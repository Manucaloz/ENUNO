import React from "react";
import Tbody from "./Tbody";

export default function CocinaComp() {
  return(
    <table className="w-60 mt-5">
        <thead className="bg-plomo txt-gris text-center">
          <tr>
            <th className="rounded-tl p-2">Pedido</th>
            <th>Mesa</th>
            <th>Cantidad</th>
            <th>Orden</th>
            <th className="rounded-tr">Estado</th>
          </tr>
        </thead>
        <Tbody />
      </table>
  );
}
