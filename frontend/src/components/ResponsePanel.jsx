// function ResponsePanel({ response }) {

//   if (!response) {
//     return (
//       <div className="card response-panel">

//         <h2>
//           Classification & Response
//         </h2>

//         <div className="empty-state">
//           No request submitted yet.
//         </div>

//       </div>
//     );
//   }

//   const agentNames = {
//     leave: "Leave Agent",
//     scheduling: "Scheduling Agent",
//     compliance: "Compliance Agent",
//     clarification: "Clarification Agent",
//   };

//   const confidence = Math.round(
//     response.confidence * 100
//   );

//   const parts = response.response.split(
//     "Context Found:"
//   );

//   const mainResponse =
//     parts[0]?.trim();

//   const context =
//     parts[1]?.trim();

//   return (
//     <div className="card response-panel">

//       <h2>
//         Classification & Response
//       </h2>

//       <div className="stats-grid">

//         <div className="intent-card">
//           <h4>Intent</h4>
//           <p>{response.intent}</p>
//         </div>

//         <div className="confidence-card">
//           <h4>Confidence</h4>
//           <p>{confidence}%</p>
//         </div>

//         <div className="agent-card">
//           <h4>Agent</h4>
//           <p>
//             {
//               agentNames[
//                 response.intent
//               ]
//             }
//           </p>
//         </div>

//         <div className="time-card">
//           <h4>Time Taken</h4>
//           <p>
//             {Number(
//               response.time_taken || 0
//             ).toFixed(2)}s
//           </p>
//         </div>

//       </div>

//       <h3>Agent Response</h3>

//       <div className="response-box">
//         <pre>{mainResponse}</pre>
//       </div>

//       {context && (

//         <>
//           <h3
//             style={{
//               marginTop: "18px",
//             }}
//           >
//             Context Used (from memory)
//           </h3>

//           <div className="context-box">
//             <pre>{context}</pre>
//           </div>
//         </>

//       )}

//     </div>
//   );
// }

// export default ResponsePanel;

function ResponsePanel({
  response,
  submittedMessage
}) {

  if (!response) {

    return (

      <div className="card response-panel">

        <h2>
          Classification & Response
        </h2>

        <div className="empty-state">
          No request submitted yet.
        </div>

      </div>

    );
  }

  const agentNames = {
    leave: "Leave Agent",
    scheduling:
      "Scheduling Agent",
    compliance:
      "Compliance Agent",
    clarification:
      "Clarification Agent",
  };

  const confidence =
    Math.round(
      response.confidence * 100
    );

  const parts =
    response.response.split(
      "Context Found:"
    );

  const mainResponse =
    parts[0]?.trim();

  return (

    <div className="card response-panel">

      <h2>
        Classification & Response
      </h2>

      <div className="stats-grid">

        <div className="intent-card">

          <h4>Intent</h4>

          <p>
            {response.intent}
          </p>

        </div>

        <div className="confidence-card">

          <h4>Confidence</h4>

          <p>
            {confidence}%
          </p>

        </div>

        <div className="agent-card">

          <h4>Agent</h4>

          <p>
            {
              agentNames[
                response.intent
              ]
            }
          </p>

        </div>

        <div className="time-card">

          <h4>
            Time Taken
          </h4>

          <p>
            {Number(
              response.time_taken ||
              0
            ).toFixed(2)}
            s
          </p>

        </div>

      </div>

      <h3>
        Agent Response
      </h3>

      <div className="response-box">

        <pre>
          {mainResponse}
        </pre>

      </div>

      {submittedMessage && (

        <>

          <h3
            style={{
              marginTop: "18px",
            }}
          >
            Current Request
          </h3>

          <div className="context-box">

            <pre>
              {submittedMessage}
            </pre>

          </div>

        </>

      )}

    </div>

  );
}

export default ResponsePanel;