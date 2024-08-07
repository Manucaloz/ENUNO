import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { AuthProvider } from '../Autenticacion/Autenticacion';
import PrivateRoute from '../Autenticacion/PrivateRoute';
import LoginPage from '../pages/Login/LoginPage';
import CorpPage from '../pages/Corporativo/CorpPage';
import AdminPage from '../pages/Administracion/AdminPage';
import PedidosPage from '../pages/Pedidos/PedidosPage';
import MesaPage from '../pages/Pedidos/MesaPage';
import CocinaPage from '../pages/cocina/CocinaPage';
import BarPage from '../pages/Bar/BarPage';
import CajaPage from '../pages/Caja/CajaPage';

export default function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path='/' element={<LoginPage />} />
          <Route path='/login' element={<LoginPage />} />
          <Route path='/corp' element={<CorpPage />} />
          <Route path='/admin' element={<AdminPage />} />
          <Route path='pedidos' element={<PedidosPage />} />
          <Route path='pedidos/mesa/:id' element={<MesaPage />} />
          <Route path='/cocina' element={<CocinaPage />} />
          <Route path='/bar' element={<BarPage />} />
          <Route path='/caja' element={<CajaPage />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}
