import axios from "axios";

const axiosInstance = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
  timeout: 10000,
  headers: {
    "Content-Type": "application/json",
  },
});

// Add a request interceptor to include the token
axiosInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("accessToken"); // Retrieve token from localStorage
    if (token) {
        console.log("Adding token to request:", token);
      config.headers.Authorization = `Bearer ${token}`;
    }
    else {
              console.warn("No token found in localStorage!");

    }
    return config;
  },
  (error) => Promise.reject(error)
);

axiosInstance.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response.status === 401 && error.response.data.code === "token_not_valid") {
      const refreshToken = localStorage.getItem("refreshToken");
      if (refreshToken) {
        try {
          const { data } = await axios.post("/token/refresh/", { refresh: refreshToken });
          localStorage.setItem("accessToken", data.access);
          error.config.headers.Authorization = `Bearer ${data.access}`;
          return axiosInstance.request(error.config); // Retry original request
        } catch (refreshError) {
          console.error("Token refresh failed:", refreshError);
          localStorage.clear();
          window.location.href = "/login"; // Redirect to login
        }
      }
    }
    return Promise.reject(error);
  }
);
export const logout = async () => {
  try {
    const refreshToken = localStorage.getItem("refresh");
    await axiosInstance.post("logout/", { refresh_token: refreshToken });
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    window.location.href = "/login"; // Redirect to login page
  } catch (error) {
    console.error("Logout failed:", error.response || error);
    alert("Logout failed. Please try again.");
  }
};
export default axiosInstance;
