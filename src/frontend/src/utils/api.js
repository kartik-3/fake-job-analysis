import axios from 'axios';
import { API_BASE_URL } from './constants';

// const config = {
// 	headers: {
// 		"Content-Type": "application/json"
// 	},
// 	withCredentials: true
// }

export async function predictJob(req) {
	console.log(req)
	const res = await axios.post(`${API_BASE_URL}/predict`, req)
	return res
}

// export async function updateFilters(req) {
// 	return await axios.post(`${API_BASE_URL}/filter_topics`, req)
// }