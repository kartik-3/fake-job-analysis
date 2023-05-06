import axios from 'axios';
import { API_BASE_URL } from './constants';

const config = {
	headers: {
		"Content-Type": "application/json"
	},
	withCredentials: true
}