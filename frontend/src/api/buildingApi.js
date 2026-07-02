import api from "./axios";

export const getBuildings = async () => {
  const response = await api.get("/buildings");
  return response.data;
};

export const getBuilding = async (id) => {
  const response = await api.get(`/buildings/${id}`);
  return response.data;
};