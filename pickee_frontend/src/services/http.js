import axios from "axios";

const APIBase = '/api';

export default {
  async getGenres() {
    const response = await axios.get(`${APIBase}/genres/`);

    return response;
  }
}