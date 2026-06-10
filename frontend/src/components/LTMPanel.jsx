import API from "../services/api";

function LTMPanel({ memory }) {

  const clearLTM = async () => {

    try {

      await API.delete(
        "/memory/ltm/1"
      );

      window.location.reload();

    } catch (error) {

      console.error(
        "Failed to clear LTM",
        error
      );
    }
  };

  return (
    <div className="memory-card inner-memory-card">

      <h3>
        Long-Term Memory
      </h3>
      <p className="memory-subtitle">
        Important Information
      </p>

      <div className="memory-list">

        {memory.length === 0 ? (

          <p>
            No long-term memories.
          </p>

        ) : (

          memory.map(
            (item, index) => (
              <div
                key={index}
                className="memory-item"
              >
                <div>
                  {item.memory}
                </div>

                <div className="score">
                  Significance Score:
                  {" "}
                  {item.score}
                </div>
              </div>
            )
          )

        )}

      </div>

      <button
        className="clear-btn"
        onClick={clearLTM}
      >
        Clear LTM
      </button>

    </div>
  );
}

export default LTMPanel;