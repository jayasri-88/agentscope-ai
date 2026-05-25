import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000")
      .then((response) => {
        setMessage(response.data.message);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <div className="h-screen bg-black text-white flex flex-col items-center justify-center">
      <h1 className="text-5xl font-bold mb-6">
        AgentScope AI
      </h1>

      <div className="bg-zinc-900 px-6 py-4 rounded-2xl shadow-lg">
        <p className="text-xl">
          Backend Response:
        </p>

        <p className="text-green-400 mt-2">
          {message}
        </p>
      </div>
    </div>
  );
}

export default App;