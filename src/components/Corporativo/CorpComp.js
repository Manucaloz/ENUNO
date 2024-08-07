import React from "react";
import Table from "./Table";

export default function CorpComp() {
  return (
    <>
      <div>
        <input className="w-100 mb-3 rounded-5 p-1 border-0 bg-gris opacity-50 px-3"
          type="text"
          placeholder="Buscar">
        </input>
      </div>
      <div className="table-responsive">
        <Table />
      </div>
      <button className="position-absolute bottom-0 start-50 translate-middle-x border-0 bg-azul text-white rounded-3 px-4 py-2"
        type="submit">
        REGISTRAR
      </button>
    </>
  );
}
