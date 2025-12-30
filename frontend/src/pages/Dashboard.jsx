import { useAuth } from "../auth/AuthContext";


import { Link } from "react-router-dom";

export default function Dashboard() {
  const { user } = useAuth();

  return (
    <>
      <h2>Welcome {user.full_name}</h2>
      {user.role === "admin" && <Link to="/admin/users">Manage Users</Link>}
      <br />
      <Link to="/profile">My Profile</Link>
    </>
  );
}
