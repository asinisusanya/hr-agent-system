// import { useState, useEffect } from "react";

// import "./App.css";

// import API from "./services/api";

// import Header from "./components/Header";
// import RequestForm from "./components/RequestForm";
// import ResponsePanel from "./components/ResponsePanel";
// import STMPanel from "./components/STMPanel";
// import LTMPanel from "./components/LTMPanel";
// import AuditTable from "./components/AuditTable";

// function App() {

//   const [userId, setUserId] = useState("1");

//   const [message, setMessage] = useState("");

//   const [response, setResponse] = useState(null);

//   const [memory, setMemory] = useState({
//     short_term_memory: [],
//     long_term_memory: [],
//   });

//   const [audit, setAudit] = useState([]);

//   const loadMemory = async () => {
//     try {

//       const res = await API.get(
//         `/memory/${userId}`
//       );

//       setMemory(res.data);

//     } catch (error) {

//       console.error(
//         "Failed to load memory",
//         error
//       );

//     }
//   };

//   const loadAudit = async () => {
//     try {

//       const res = await API.get(
//         "/audit"
//       );

//       setAudit(res.data);

//     } catch (error) {

//       console.error(
//         "Failed to load audit logs",
//         error
//       );

//     }
//   };

//   const submitRequest = async () => {

//     if (!message.trim()) return;

//     try {

//       const res = await API.post(
//         "/request",
//         {
//           user_id: userId,
//           message,
//         }
//       );

//       setResponse(res.data);

//       await loadMemory();

//       await loadAudit();

//       setMessage("");

//     } catch (error) {

//       console.error(
//         "Request failed",
//         error
//       );

//     }
//   };

//   useEffect(() => {

//     loadMemory();

//     loadAudit();

//   }, []);

//   return (

//     <div className="container">

//       <Header />

//       {/* Top Section */}

//       <div className="top-grid">

//         <RequestForm
//           userId={userId}
//           setUserId={setUserId}
//           message={message}
//           setMessage={setMessage}
//           onSubmit={submitRequest}
//         />

//         <ResponsePanel
//           response={response}
//         />

//       </div>

//       {/* Bottom Section */}

//       <div className="middle-grid">

//         {/* Memory Card */}

//         <div className="card memory-wrapper">

//           <h2>Memory</h2>

//           <div className="memory-grid">

//             <STMPanel
//               userId={userId}
//               memory={memory.short_term_memory}
//               reloadMemory={loadMemory}
//             />

//             <LTMPanel
//               userId={userId}
//               memory={memory.long_term_memory}
//               reloadMemory={loadMemory}
//             />

//           </div>

//         </div>

//         {/* Audit Logs */}

//         <AuditTable
//           audit={audit}
//         />

//       </div>

//     </div>

//   );
// }

// export default App;

import { useState, useEffect } from "react";

import "./App.css";

import API from "./services/api";

import Header from "./components/Header";
import RequestForm from "./components/RequestForm";
import ResponsePanel from "./components/ResponsePanel";
import STMPanel from "./components/STMPanel";
import LTMPanel from "./components/LTMPanel";
import AuditTable from "./components/AuditTable";

function App() {

  const [userId, setUserId] =
    useState("1");

  const [message, setMessage] =
    useState("");

  const [submittedMessage,
    setSubmittedMessage] =
    useState("");

  const [response, setResponse] =
    useState(null);

  const [memory, setMemory] =
    useState({
      short_term_memory: [],
      long_term_memory: [],
    });

  const [audit, setAudit] =
    useState([]);

  const loadMemory = async () => {

    try {

      const res =
        await API.get(
          `/memory/${userId}`
        );

      setMemory(res.data);

    } catch (error) {

      console.error(
        "Failed to load memory",
        error
      );

    }
  };

  const loadAudit = async () => {

    try {

      const res =
        await API.get(
          "/audit"
        );

      setAudit(res.data);

    } catch (error) {

      console.error(
        "Failed to load audit logs",
        error
      );

    }
  };

  const submitRequest = async () => {

    if (!message.trim())
      return;

    try {

      const res =
        await API.post(
          "/request",
          {
            user_id: userId,
            message,
          }
        );

      setSubmittedMessage(
        message
      );

      setResponse(
        res.data
      );

      await loadMemory();

      await loadAudit();

      setMessage("");

    } catch (error) {

      console.error(
        "Request failed",
        error
      );

    }
  };

  useEffect(() => {

    loadMemory();

    loadAudit();

  }, []);

  return (

    <div className="container">

      <Header />

      <div className="top-grid">

        <RequestForm
          userId={userId}
          setUserId={setUserId}
          message={message}
          setMessage={setMessage}
          onSubmit={submitRequest}
        />

        <ResponsePanel
          response={response}
          submittedMessage={
            submittedMessage
          }
        />

      </div>

      <div className="middle-grid">

        <div className="card memory-wrapper">

          <h2>Memory</h2>

          <div className="memory-grid">

            <STMPanel
              userId={userId}
              memory={
                memory.short_term_memory
              }
              reloadMemory={
                loadMemory
              }
            />

            <LTMPanel
              userId={userId}
              memory={
                memory.long_term_memory
              }
              reloadMemory={
                loadMemory
              }
            />

          </div>

        </div>

        <AuditTable
          audit={audit}
        />

      </div>

    </div>

  );
}

export default App;