function RequestForm({
  userId,
  setUserId,
  message,
  setMessage,
  onSubmit,
}) {
  return (
    <div className="card request-card">

      <h2>Submit Request</h2>

      <label>User ID</label>

      <input
        type="text"
        value={userId}
        onChange={(e) =>
          setUserId(e.target.value)
        }
      />

      <label>Message</label>

      <textarea
        placeholder="Type your request here..."
        value={message}
        onChange={(e) =>
          setMessage(e.target.value)
        }
      />

      <button onClick={onSubmit}>
        Submit Request
      </button>

      <div
        style={{
          marginTop: "15px",
          fontSize: "13px",
          color: "#64748b",
        }}
      >
        Examples:
        <br />
        "Can I take leave tomorrow?"
        <br />
        "Schedule a meeting"
        <br />
        "What are the company rules for remote work?"
      </div>

    </div>
  );
}

export default RequestForm;