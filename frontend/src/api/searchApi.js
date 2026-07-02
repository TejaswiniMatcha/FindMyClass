import api from "./axios";

export const searchCampus = async (query) => {
    const { data } = await api.get("/search", {
        params: {
            q: query,
        },
    });

    return data.results;
};