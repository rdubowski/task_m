import axios from "axios";



export const encodeUrl = async (base_url) => {
    const url = "http://localhost:8004/encode/";
    const data = {"base_url": base_url};
    try {
      const response = await axios.post(url, data, {
        "Content-Type": "application/json",
      });
      return response.data.shortened_url
    } catch (error) {
        console.error('Error:', error.response ? error.response.data : error);
    }
  };



  export const decodeUrl = async (shortened_url) => {
    const url = "http://localhost:8004/decode/";
    const data = {"shortened_url": shortened_url};
    try {
      const response = await axios.post(url, data, {
        "Content-Type": "application/json",
      });
      return response.data.base_url
    } catch (error) {
      console.error('Error:', error.response ? error.response.data : error);
    }
  };