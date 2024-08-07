import React from "react";
import Header from '../../components/Header/Header';
import Footer from "../../components/Footer/Footer";
import AdminComp from "../../components/Administracion/AdminComp";
import '../../assets/style.css';

export default function AdminPage() {
  return (
    <>
      <div id="body">
        <header id="header">
          <Header />
        </header>
        <main id="main" className="d-flex justify-content-center position-relative">
          <div>
            <AdminComp />
          </div>
        </main>
        <footer id="footer">
          <Footer />
        </footer>
      </div>
    </>
  );
}
