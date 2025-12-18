import { useState } from "react";

export default function App() {
  // Escribe tu solución aquí
  const [value, setValue] = useState(0)
  return (
    <div className="container">

      <p className="value">{value}</p>

      <div className="container-buttons">
        <button onClick={() => setValue(value + 1)}>Incrementar</button>
        <button onClick={() => setValue(value - 1)}>Decrementar</button>
        <button onClick={() => setValue(0)}>Reset</button>
      </div>
    </div>
  )
}
