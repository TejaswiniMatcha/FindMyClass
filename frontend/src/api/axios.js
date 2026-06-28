import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
    headers: {
        "Content-Type": "application/json",
    },
});

export default api;

// ADD THIS 👇
export const searchCampus = async (query) => {
    const res = await api.get(`/search?q=${query}`);
    return res.data;
};