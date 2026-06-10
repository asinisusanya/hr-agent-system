// function AuditTable({ audit }) {
//   return (
//     <div className="card audit-card">

//       <h2>Audit Logs</h2>

//       <div className="audit-table-container">

//         <table className="audit-table">

//           <thead>
//             <tr>
//               <th>User ID</th>
//               <th>Request</th>
//               <th>Intent</th>
//               <th>Agent</th>
//               <th>Confidence</th>
//               <th>Status</th>
//             </tr>
//           </thead>

//           <tbody>

//             {audit.length === 0 ? (

//               <tr>
//                 <td
//                   colSpan="6"
//                   style={{
//                     textAlign: "center",
//                     padding: "20px"
//                   }}
//                 >
//                   No audit logs available.
//                 </td>
//               </tr>

//             ) : (

//               audit.map((item, index) => (

//                 <tr key={index}>

//                   <td>{item.user_id}</td>

//                   <td>
//                     {item.request?.length > 40
//                       ? item.request.substring(0, 40) + "..."
//                       : item.request}
//                   </td>

//                   <td>{item.intent}</td>

//                   <td>{item.agent}</td>

//                   <td>
//                     {item.confidence}
//                   </td>

//                   <td>

//                     <span
//                       className={
//                         item.status === "SUCCESS"
//                           ? "status-success"
//                           : "status-error"
//                       }
//                     >
//                       {item.status}
//                     </span>

//                   </td>

//                 </tr>

//               ))

//             )}

//           </tbody>

//         </table>

//       </div>

//     </div>
//   );
// }

// export default AuditTable;

function AuditTable({ audit }) {

  return (

    <div className="card audit-card">

      <h2>Audit Logs</h2>

      <div className="audit-table-container">

        <table className="audit-table">

          <thead>

            <tr>

              <th>ID</th>

              <th>Time</th>

              <th>User ID</th>

              <th>Request</th>

              <th>Intent</th>

              <th>Agent</th>

              <th>Confidence</th>

              <th>Status</th>

            </tr>

          </thead>

          <tbody>

            {audit.length === 0 ? (

              <tr>

                <td
                  colSpan="8"
                  style={{
                    textAlign: "center",
                    padding: "20px"
                  }}
                >
                  No audit logs available.
                </td>

              </tr>

            ) : (

              audit.map((item, index) => (

                <tr key={index}>

                  <td>{item.id}</td>

                  <td>
                    {item.timestamp
                      ? new Date(
                          item.timestamp
                        ).toLocaleString()
                      : "-"}
                  </td>

                  <td>{item.user_id}</td>

                  <td>

                    {item.request?.length > 40
                      ? item.request.substring(
                          0,
                          40
                        ) + "..."
                      : item.request}

                  </td>

                  <td>{item.intent}</td>

                  <td>{item.agent}</td>

                  <td>

                    {item.confidence
                      ? (
                          item.confidence *
                          100
                        ).toFixed(0) + "%"
                      : "-"}

                  </td>

                  <td>

                    <span
                      className={
                        item.status ===
                        "SUCCESS"
                          ? "status-success"
                          : "status-error"
                      }
                    >
                      {item.status}
                    </span>

                  </td>

                </tr>

              ))

            )}

          </tbody>

        </table>

      </div>

    </div>

  );

}

export default AuditTable;