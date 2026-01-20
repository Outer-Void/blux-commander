import React, { useCallback, useEffect, useRef, useState } from "https://esm.sh/react@18.3.1";
import { createRoot } from "https://esm.sh/react-dom@18.3.1/client";

const h = React.createElement;
const API_BASE = `${window.location.origin}/api`;

function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try {
      const stored = window.localStorage.getItem(key);
      return stored ?? initialValue;
    } catch (error) {
      console.warn("Unable to access localStorage", error);
      return initialValue;
    }
  });

  const setItem = useCallback(
    (next) => {
      setValue((prev) => {
        const resolved = typeof next === "function" ? next(prev) : next;
        try {
          if (resolved === null || resolved === undefined) {
            window.localStorage.removeItem(key);
          } else {
            window.localStorage.setItem(key, resolved);
          }
        } catch (error) {
          console.warn("Failed to persist localStorage value", error);
        }
        return resolved;
      });
    },
    [key],
  );

  return [value, setItem];
}

function SectionCard({ title, description, actions, children }) {
  return h(
    "section",
    { className: "rounded-xl border border-slate-800 bg-slate-900/60 p-6 shadow-lg shadow-slate-950/40" },
    h(
      "div",
      { className: "mb-4 flex flex-col gap-2 md:flex-row md:items-center md:justify-between" },
      h("div", {}, h("h2", { className: "text-xl font-semibold" }, title), description && h("p", { className: "text-sm text-slate-400" }, description)),
      actions && h("div", { className: "flex items-center gap-2" }, actions),
    ),
    children,
  );
}

function Button({ children, onClick, type = "button", variant = "default", disabled }) {
  const styles =
    variant === "secondary"
      ? "border border-slate-700 bg-slate-800 hover:bg-slate-700"
      : variant === "ghost"
        ? "hover:bg-slate-800"
        : "bg-primary-500 hover:bg-primary-400 text-slate-950";
  return h(
    "button",
    {
      type,
      onClick,
      disabled,
      className: `inline-flex items-center justify-center rounded-lg px-4 py-2 text-sm font-medium transition focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-400 disabled:cursor-not-allowed disabled:opacity-60 ${styles}`,
    },
    children,
  );
}

function useAuthenticatedFetch(token) {
  return useCallback(
    async (path, options = {}) => {
      const headers = new Headers(options.headers || {});
      if (token) {
        headers.set("X-BLUX-Key", token);
      }
      const response = await fetch(`${API_BASE}${path}`, { ...options, headers });
      if (!response.ok) {
        const errorBody = await response.json().catch(() => ({}));
        throw new Error(errorBody.detail || `Request failed with status ${response.status}`);
      }
      return response.json();
    },
    [token],
  );
}

function useBootstrap() {
  const [bootstrap, setBootstrap] = useState({ loading: true, data: null, error: null });
  useEffect(() => {
    let active = true;
    fetch(`${API_BASE}/auth/keypair`)
      .then((resp) => resp.json())
      .then((data) => {
        if (active) setBootstrap({ loading: false, data, error: null });
      })
      .catch((error) => {
        console.error("Failed to load keypair", error);
        if (active) setBootstrap({ loading: false, data: null, error });
      });
    return () => {
      active = false;
    };
  }, []);
  return bootstrap;
}

function CommandConsole({ token, onExecuted }) {
  const [command, setCommand] = useState("plugins list");
  const [repo, setRepo] = useState("");
  const [result, setResult] = useState(null);
  const [streamMessages, setStreamMessages] = useState([]);
  const [streaming, setStreaming] = useState(false);
  const wsRef = useRef(null);
  const fetcher = useAuthenticatedFetch(token);

  const connectSocket = useCallback(() => {
    if (!token) return;
    const wsUrl = new URL(`${window.location.origin.replace(/^http/, "ws")}/ws/commands`);
    wsUrl.searchParams.set("token", token);
    const socket = new WebSocket(wsUrl);
    socket.onopen = () => {
      setStreamMessages((messages) => [...messages, { type: "system", message: "Connected to command stream" }]);
    };
    socket.onmessage = (event) => {
      try {
        const payload = JSON.parse(event.data);
        setStreamMessages((messages) => [...messages, payload]);
        if (payload.type === "exit") {
          setStreaming(false);
        }
      } catch (error) {
        console.warn("Unable to parse websocket payload", error);
      }
    };
    socket.onclose = () => {
      setStreamMessages((messages) => [...messages, { type: "system", message: "Stream disconnected" }]);
    };
    socket.onerror = () => {
      setStreamMessages((messages) => [...messages, { type: "error", message: "Stream error" }]);
    };
    wsRef.current = socket;
  }, [token]);

  useEffect(() => {
    connectSocket();
    return () => {
      if (wsRef.current) {
        wsRef.current.close();
      }
    };
  }, [connectSocket]);

  const runCommand = useCallback(
    async (event) => {
      event.preventDefault();
      if (!command) return;
      try {
        const body = { command, repo: repo || null };
        const response = await fetcher("/commands/execute", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(body),
        });
        setResult(response.result);
        onExecuted?.();
      } catch (error) {
        setResult({ error: [error.message], output: [], exit_code: 1, command });
      }
    },
    [command, repo, fetcher, onExecuted],
  );

  const runStreaming = useCallback(() => {
    if (!command || !wsRef.current || wsRef.current.readyState !== WebSocket.OPEN) {
      setStreamMessages((messages) => [...messages, { type: "error", message: "Command stream unavailable" }]);
      return;
    }
    setStreaming(true);
    setStreamMessages((messages) => [
      ...messages,
      { type: "system", message: `→ ${command}${repo ? ` @ ${repo}` : ""}` },
    ]);
    wsRef.current.send(JSON.stringify({ command, repo: repo || null }));
  }, [command, repo]);

  return SectionCard(
    {
      title: "Command Center",
      description: "Execute bq-cli commands and inspect plugin output in real-time.",
      actions: h(
        Button,
        { variant: "secondary", onClick: runStreaming, disabled: !token || streaming },
        streaming ? "Streaming..." : "Run Stream",
      ),
    },
    h(
      "form",
      { onSubmit: runCommand, className: "flex flex-col gap-4" },
      h(
        "div",
        { className: "grid gap-4 md:grid-cols-[1fr_minmax(0,200px)_auto]" },
        h("input", {
          className: "w-full rounded-lg border border-slate-700 bg-slate-950/80 px-3 py-2 text-sm",
          placeholder: "Command (e.g., plugins list)",
          value: command,
          onChange: (event) => setCommand(event.target.value),
        }),
        h("input", {
          className: "rounded-lg border border-slate-700 bg-slate-950/80 px-3 py-2 text-sm",
          placeholder: "Repository path (optional)",
          value: repo,
          onChange: (event) => setRepo(event.target.value),
        }),
        h(Button, { type: "submit", disabled: !token }, "Run once"),
      ),
      result &&
        h(
          "div",
          { className: "grid gap-4 md:grid-cols-2" },
          h(ResultBlock, { title: "stdout", lines: result.output || [] }),
          h(ResultBlock, { title: "stderr", lines: result.error || [] }),
        ),
      h(StreamLog, { messages: streamMessages }),
    ),
  );
}

function ResultBlock({ title, lines }) {
  if (!lines.length) {
    return h(
      "div",
      { className: "rounded-lg border border-slate-800 bg-slate-950/80 p-3" },
      h("p", { className: "text-xs uppercase tracking-wide text-slate-500" }, title),
      h("p", { className: "mt-2 text-sm text-slate-500" }, "No output"),
    );
  }
  return h(
    "div",
    { className: "rounded-lg border border-slate-800 bg-slate-950/80 p-3" },
    h("p", { className: "text-xs uppercase tracking-wide text-slate-500" }, title),
    h(
      "pre",
      { className: "mt-2 overflow-x-auto whitespace-pre-wrap break-words text-sm leading-relaxed" },
      lines.join("\n"),
    ),
  );
}

function StreamLog({ messages }) {
  if (!messages.length) return null;
  return h(
    "div",
    { className: "rounded-lg border border-slate-800 bg-slate-950/80 p-3" },
    h("p", { className: "text-xs uppercase tracking-wide text-slate-500" }, "Live Stream"),
    h(
      "div",
      { className: "mt-3 max-h-60 space-y-2 overflow-y-auto text-sm" },
      messages.map((message, index) =>
        h(
          "div",
          { key: index, className: message.type === "error" ? "text-red-400" : "text-slate-200" },
          h("span", { className: "mr-2 text-xs uppercase text-slate-500" }, message.type || "log"),
          message.message || JSON.stringify(message),
        ),
      ),
    ),
  );
}

function RepoInsights({ token, onRefresh, data, refreshSignal = 0 }) {
  const fetcher = useAuthenticatedFetch(token);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const refresh = useCallback(async () => {
    if (!token) return;
    setLoading(true);
    setError(null);
    try {
      const response = await fetcher("/repos");
      onRefresh(response.repos);
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  }, [token, fetcher, onRefresh]);

  useEffect(() => {
    refresh();
  }, [refresh, refreshSignal]);

  return SectionCard(
    {
      title: "Repository Insights",
      description: "Track multiple BLUX project workspaces and git health.",
      actions: h(Button, { variant: "secondary", onClick: refresh, disabled: loading || !token }, loading ? "Refreshing" : "Refresh"),
    },
    h(
      "div",
      { className: "grid gap-4" },
      error && h("p", { className: "text-sm text-red-400" }, error.message),
      (data || []).length === 0 && !loading
        ? h(
            "div",
            { className: "rounded-lg border border-dashed border-slate-800 p-4 text-sm text-slate-400" },
            "No repositories registered yet. Use the form below to add one.",
          )
        : (data || []).map((repo) => h(RepoCard, { key: repo.name, repo })),
    ),
  );
}

function RepoCard({ repo }) {
  return h(
    "article",
    { className: "rounded-lg border border-slate-800 bg-slate-950/80 p-4" },
    h("div", { className: "flex items-start justify-between" }, h("h3", { className: "text-lg font-semibold" }, repo.name), h("span", { className: "rounded-full bg-primary-500/10 px-3 py-1 text-xs font-medium text-primary-300" }, repo.branch || "unknown")),
    repo.description && h("p", { className: "mt-2 text-sm text-slate-400" }, repo.description),
    h(
      "dl",
      { className: "mt-4 grid grid-cols-2 gap-4 text-sm" },
      h(StatCell, { label: "Dirty", value: repo.dirty ? "Yes" : "No" }),
      h(StatCell, { label: "Ahead", value: repo.ahead_commits ?? "–" }),
      h(StatCell, { label: "Tracked files", value: repo.tracked_files ?? "–" }),
      h(StatCell, { label: "Size", value: repo.size_bytes ? formatBytes(repo.size_bytes) : "–" }),
      h(StatCell, { label: "Latest", value: repo.latest_commit ?? "–", wide: true }),
      h(StatCell, { label: "Path", value: repo.path, wide: true }),
    ),
  );
}

function StatCell({ label, value, wide }) {
  return h(
    "div",
    { className: `rounded-md border border-slate-800 bg-slate-950/60 p-3 ${wide ? "col-span-2" : ""}` },
    h("dt", { className: "text-xs uppercase tracking-wide text-slate-500" }, label),
    h("dd", { className: "mt-1 text-sm text-slate-200" }, value),
  );
}

function formatBytes(bytes) {
  if (!bytes) return "0 B";
  const units = ["B", "KB", "MB", "GB", "TB"];
  let index = 0;
  let value = bytes;
  while (value >= 1024 && index < units.length - 1) {
    value /= 1024;
    index += 1;
  }
  return `${value.toFixed(1)} ${units[index]}`;
}

function PluginRegistry({ token }) {
  const [plugins, setPlugins] = useState([]);
  const [error, setError] = useState(null);
  const fetcher = useAuthenticatedFetch(token);

  const refresh = useCallback(async () => {
    if (!token) return;
    setError(null);
    try {
      const response = await fetcher("/plugins");
      setPlugins(response.plugins || []);
    } catch (err) {
      setError(err);
    }
  }, [token, fetcher]);

  useEffect(() => {
    refresh();
  }, [refresh]);

  return SectionCard(
    {
      title: "Plugin Registry",
      description: "Discover installed BLUX extensions registered via entry points.",
      actions: h(Button, { variant: "secondary", onClick: refresh, disabled: !token }, "Refresh"),
    },
    error && h("p", { className: "text-sm text-red-400" }, error.message),
    h(
      "ul",
      { className: "mt-4 space-y-2 text-sm" },
      plugins.length === 0
        ? h("li", { className: "text-slate-400" }, "No plugins detected. Register entry points via 'blux.plugins'.")
        : plugins.map((plugin) => h("li", { key: plugin, className: "rounded-md border border-slate-800 bg-slate-950/60 px-3 py-2" }, plugin)),
    ),
  );
}

function MemoryReplay({ entries }) {
  return SectionCard(
    {
      title: "Memory Replay",
      description: "Chronological view of recent command executions stored locally.",
    },
    entries.length === 0
      ? h("p", { className: "text-sm text-slate-400" }, "No command memory recorded yet. Execute commands to populate history." )
      : h(
          "div",
          { className: "space-y-4" },
          entries.map((entry, index) =>
            h(
              "article",
              { key: index, className: "rounded-lg border border-slate-800 bg-slate-950/70 p-4" },
              h("header", { className: "flex flex-wrap items-center justify-between gap-2" },
                h("span", { className: "rounded-md bg-primary-500/10 px-2 py-1 text-xs font-medium text-primary-300" }, entry.command),
                h("time", { className: "text-xs text-slate-500" }, entry.timestamp),
              ),
              entry.repo && h("p", { className: "mt-2 text-xs text-slate-400" }, `Repo: ${entry.repo}`),
              h(
                "div",
                { className: "mt-3 grid gap-3 md:grid-cols-2" },
                h(ResultBlock, { title: "stdout", lines: entry.output || [] }),
                h(ResultBlock, { title: "stderr", lines: entry.error || [] }),
              ),
              h(
                "p",
                { className: "mt-2 text-xs text-slate-500" },
                `Exit ${entry.exit_code} · ${typeof entry.duration_seconds === "number" ? entry.duration_seconds.toFixed(2) : "0.00"}s`,
              ),
            ),
          ),
        ),
  );
}

function RepoForm({ token, onAdded }) {
  const [name, setName] = useState("");
  const [path, setPath] = useState("");
  const [description, setDescription] = useState("");
  const [error, setError] = useState(null);
  const fetcher = useAuthenticatedFetch(token);

  const submit = useCallback(
    async (event) => {
      event.preventDefault();
      if (!name || !path) {
        setError(new Error("Name and path are required"));
        return;
      }
      setError(null);
      try {
        await fetcher("/repos", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ name, path, description: description || null }),
        });
        setName("");
        setPath("");
        setDescription("");
        onAdded?.();
      } catch (err) {
        setError(err);
      }
    },
    [name, path, description, fetcher, onAdded],
  );

  return SectionCard(
    {
      title: "Add Repository",
      description: "Register a local BLUX project to include it in insights.",
    },
    h(
      "form",
      { className: "grid gap-4 md:grid-cols-3", onSubmit: submit },
      h("input", {
        className: "rounded-lg border border-slate-700 bg-slate-950/80 px-3 py-2 text-sm",
        placeholder: "Display name",
        value: name,
        onChange: (event) => setName(event.target.value),
      }),
      h("input", {
        className: "rounded-lg border border-slate-700 bg-slate-950/80 px-3 py-2 text-sm",
        placeholder: "Path to repo",
        value: path,
        onChange: (event) => setPath(event.target.value),
      }),
      h(Button, { type: "submit", disabled: !token }, "Add"),
      h("textarea", {
        className: "col-span-3 min-h-[80px] rounded-lg border border-slate-700 bg-slate-950/80 px-3 py-2 text-sm",
        placeholder: "Optional description", value: description,
        onChange: (event) => setDescription(event.target.value),
      }),
      error && h("p", { className: "col-span-3 text-sm text-red-400" }, error.message),
    ),
  );
}

function AuthenticationPanel({ bootstrap, token, setToken }) {
  const [input, setInput] = useState(token || "");
  const [status, setStatus] = useState(null);

  const submit = useCallback(
    async (event) => {
      event.preventDefault();
      if (!input) return;
      try {
        const response = await fetch(`${API_BASE}/auth/session`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ token: input }),
        });
        if (!response.ok) {
          const errorBody = await response.json().catch(() => ({}));
          throw new Error(errorBody.detail || "Authentication failed");
        }
        setToken(input);
        setStatus("Authenticated");
      } catch (error) {
        setStatus(error.message);
      }
    },
    [input, setToken],
  );

  return SectionCard(
    {
      title: "Local Keypair Authentication",
      description: "Paste the private key stored under ~/.config/blux-commander/keypair.json to unlock the dashboard.",
      actions: bootstrap.data &&
        h(
          "a",
          {
            className: "text-xs font-medium text-primary-300 hover:text-primary-200",
            href: "#",
            onClick: (event) => {
              event.preventDefault();
              navigator.clipboard?.writeText(bootstrap.data.public_key || "");
              setStatus("Public key copied");
            },
          },
          "Copy public key",
        ),
    },
    h(
      "form",
      { className: "flex flex-col gap-4", onSubmit: submit },
      h("p", { className: "text-sm text-slate-300" }, "Your private key never leaves this device. Keys are generated automatically when the server starts."),
      bootstrap.loading
        ? h("p", { className: "text-sm text-slate-400" }, "Generating keypair…")
        : bootstrap.error
          ? h("p", { className: "text-sm text-red-400" }, "Failed to bootstrap keypair. Check server logs.")
          : h(
              "div",
              { className: "grid gap-3 md:grid-cols-[1fr_auto]" },
              h("input", {
                className: "w-full rounded-lg border border-slate-700 bg-slate-950/80 px-3 py-2 text-sm",
                placeholder: "Private key",
                value: input,
                onChange: (event) => setInput(event.target.value.trim()),
              }),
              h(Button, { type: "submit" }, "Unlock"),
              h(
                "p",
                { className: "md:col-span-2 text-xs text-slate-500" },
                `Keys stored at ${bootstrap.data?.config_dir ?? '~/.config/blux-commander'}`,
              ),
            ),
      status && h("p", { className: "text-xs text-slate-400" }, status),
    ),
  );
}

function Dashboard() {
  const bootstrap = useBootstrap();
  const [token, setToken] = useLocalStorage("blux-commander-key", "");
  const [repos, setRepos] = useState([]);
  const [memory, setMemory] = useState([]);
  const [repoSignal, setRepoSignal] = useState(0);

  const fetcher = useAuthenticatedFetch(token);

  const refreshMemory = useCallback(async () => {
    if (!token) return;
    try {
      const response = await fetcher("/memory/replay");
      setMemory(response.entries || []);
    } catch (error) {
      console.warn("Failed to refresh memory", error);
    }
  }, [token, fetcher]);

  useEffect(() => {
    refreshMemory();
  }, [refreshMemory]);

  const statusBanner = bootstrap.data
    ? h(
        "div",
        { className: "rounded-xl border border-primary-500/20 bg-primary-500/10 px-6 py-4" },
        h("p", { className: "text-sm text-primary-100" }, "BLUX Commander is ready. Authenticate to access orchestration tools."),
      )
    : null;

  return h(
    "main",
    { className: "mx-auto flex min-h-screen w-full max-w-6xl flex-col gap-8 px-6 py-10" },
    h(
      "header",
      { className: "flex flex-col gap-4 md:flex-row md:items-center md:justify-between" },
      h("div", {}, h("h1", { className: "text-3xl font-bold" }, "BLUX Commander"), h("p", { className: "text-sm text-slate-400" }, "Unified cockpit for orchestrating BLUX projects.")),
      bootstrap.data && h("span", { className: "rounded-full bg-slate-800 px-4 py-2 text-xs text-slate-300" }, `Public key: ${bootstrap.data.public_key.slice(0, 8)}…`),
    ),
    statusBanner,
    h(AuthenticationPanel, { bootstrap, token, setToken }),
    token
      ? h(
          React.Fragment,
          {},
          h(CommandConsole, { token, onExecuted: refreshMemory }),
          h(RepoForm, {
            token,
            onAdded: () => {
              setRepoSignal((value) => value + 1);
              setTimeout(() => {
                refreshMemory();
              }, 100);
            },
          }),
          h(RepoInsights, { token, data: repos, onRefresh: setRepos, refreshSignal: repoSignal }),
          h(PluginRegistry, { token }),
          h(MemoryReplay, { entries: memory }),
        )
      : h(
          "p",
          { className: "text-sm text-slate-400" },
          "Authenticate with your private key to load project insights, command history, and live orchestration tools.",
        ),
  );
}

const container = document.getElementById("root");
if (container) {
  const root = createRoot(container);
  root.render(h(Dashboard));
}
