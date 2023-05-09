import axios from "axios";
import { API_BASE_URL } from "./constants";

export async function predictJob(req) {
  return await axios.post(`${API_BASE_URL}/predict`, req);
}

export async function getJobData() {
  return await axios.get(`${API_BASE_URL}/predict`);
}

export async function confidence(min, max) {
  return Math.round(((Math.random() * (max - min) + min) + Number.EPSILON) * 100) / 100
}
