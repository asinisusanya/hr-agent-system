function MemoryPanel({ memory }) {
  return (
    <div className="card">
      <h2>Memory</h2>

      <h3>Short-Term Memory</h3>

      <ul>
        {memory.short_term_memory?.map(
          (item, index) => (
            <li key={index}>
              {item.message}
            </li>
          )
        )}
      </ul>

      <h3>Long-Term Memory</h3>

      <ul>
        {memory.long_term_memory?.map(
          (item, index) => (
            <li key={index}>
              {item.memory}
              <br />
              Score: {item.score}
            </li>
          )
        )}
      </ul>
    </div>
  );
}

export default MemoryPanel;