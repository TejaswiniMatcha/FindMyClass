import api from "./axios";

export const searchCampus = async (query) => {
  const response = await api.get("/search", {
    params: {
      q: query,
    },
  });

  return response.data;
};

export const autocompleteCampus = async (query) => {
  const response = await api.get("/autocomplete", {
    params: {
      query,
    },
  });

  return response.data;
};