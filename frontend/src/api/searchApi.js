import api from "./axios";

export const searchCampus = async (query) => {
    const { data } = await api.get("/search", {
        params: {
            q: query,
        },
    });

    return data.results;
};

export const searchCampusSuggestions = async (query, limit = 8) => {
    const { data } = await api.get("/search/suggestions", {
        params: {
            q: query,
            limit,
        },
    });

    return data.results;
};