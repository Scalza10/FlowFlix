import { createStore } from "vuex";
import { jwtDecode } from "jwt-decode";

export default createStore({
  state: {
    username: "",
  },
  mutations: {
    setUsername(state, username) {
      state.username = username;
    },
  },
  actions: {
    login({ commit }, token) {
      const decoded = jwtDecode(token);
      commit("setUsername", decoded.sub.username);
      localStorage.setItem("access_token", token);
    },
    logout({ commit }) {
      commit("setUsername", "");
      localStorage.removeItem("access_token");
    },
    initialize({ commit }) {
      const token = localStorage.getItem("access_token");
      if (token) {
        const decoded = jwtDecode(token);
        commit("setUsername", decoded.username);
      }
    },
  },
  getters: {
    username: (state) => state.username,
  },
});
