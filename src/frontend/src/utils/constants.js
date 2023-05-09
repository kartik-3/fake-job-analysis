// Constants
export const API_BASE_URL = 'http://0.0.0.0:5000';

export const confidence = (l, h) => {
  return Math.round(((Math.random() * (h - l) + l) + Number.EPSILON) * 100) / 100
}