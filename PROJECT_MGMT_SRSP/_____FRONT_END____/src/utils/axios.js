import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/', // Django backend API
    timeout: 10000,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Add request interceptor to attach the token
axiosInstance.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('accessToken');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// Add response interceptor for handling token expiry
axiosInstance.interceptors.response.use(
    (response) => response,
    async (error) => {
        if (error.response.status === 401 && error.response.data.code === 'token_not_valid') {
            const refreshToken = localStorage.getItem('refreshToken');
            if (refreshToken) {
                try {
                    const { data } = await axios.post('http://127.0.0.1:8000/api/token/refresh/', {
                        refresh: refreshToken,
                    });
                    localStorage.setItem('accessToken', data.access);
                    // Retry the failed request with the new token
                    error.config.headers.Authorization = `Bearer ${data.access}`;
                    return axiosInstance.request(error.config);
                } catch (refreshError) {
                    console.error('Token refresh failed:', refreshError);
                    localStorage.clear();
                    window.location.href = '/'; // Redirect to login
                }
            }
        }
        return Promise.reject(error);
    }
);

export default axiosInstance;
