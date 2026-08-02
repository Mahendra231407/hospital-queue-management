import { useEffect, useState } from "react";
import apiClient from "../api/client";

function HealthStatus() {
  const [isConnected, setIsConnected] = useState(null);

  useEffect(() => {
    const checkHealth = async () => {
      try {
        const response = await apiClient.get("/api/health");
        const isHealthy =
          response.data.status === "ok" &&
          response.data.database === "connected";
        setIsConnected(isHealthy);
      } catch {
        setIsConnected(false);
      }
    };

    checkHealth();
  }, []);

  if (isConnected === null) {
    return <p className="health-status loading">Checking backend status...</p>;
  }

  if (isConnected) {
    return <p className="health-status connected">🟢 Backend Connected</p>;
  }

  return <p className="health-status disconnected">🔴 Backend Disconnected</p>;
}

export default HealthStatus;
