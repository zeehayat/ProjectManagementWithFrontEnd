import { createStore } from "vuex";

export default createStore({
  state: {
    isAuthenticated: !!localStorage.getItem("accessToken"),
  },
  mutations: {
    setAuthenticated(state, status) {
      state.isAuthenticated = status;
    },
  },
  actions: {
    login({ commit }, token) {
      localStorage.setItem("accessToken", token);
      commit("setAuthenticated", true);
    },
    logout({ commit }) {
      localStorage.removeItem("accessToken");
      //localStorage.removeItem("refreshToken");
      commit("setAuthenticated", false);
    },
  },
});
