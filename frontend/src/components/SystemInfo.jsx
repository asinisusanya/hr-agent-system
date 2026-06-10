function SystemInfo() {
  return (
    <div className="card">
      <h2>System Information</h2>

      <div className="system-info">
        <div>
          <strong>Model</strong>
          <p>Gemini 2.5 Flash</p>
        </div>

        <div>
          <strong>Workflow</strong>
          <p>LangGraph</p>
        </div>

        <div>
          <strong>Database</strong>
          <p>SQLite</p>
        </div>

        <div>
          <strong>Memory</strong>
          <p>STM + LTM</p>
        </div>
      </div>
    </div>
  );
}

export default SystemInfo;