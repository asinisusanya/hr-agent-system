import API from "../services/api";

function STMPanel({ memory }) {

  const clearSTM = async () => {

    try {

      await API.delete(
        "/memory/stm/1"
      );

      window.location.reload();

    } catch (error) {

      console.error(
        "Failed to clear STM",
        error
      );
    }
  };

  return (
    <div className="memory-card inner-memory-card">

      <h3>
        Short-Term Memory
      </h3>

      <p className="memory-subtitle">
        Recent Conversations
      </p>
      

      <div className="memory-list">

        {memory.length === 0 ? (

          <p>
            No short-term memories.
          </p>

        ) : (

          memory.map(
            (item, index) => (
              <div
                key={index}
                className="memory-item"
              >
                {item.message}
              </div>
            )
          )

        )}

      </div>

      <button
        className="clear-btn"
        onClick={clearSTM}
      >
        Clear STM
      </button>

    </div>
  );
}

export default STMPanel;