// Storing states, mutations, actions
const state = {
  dataByCols: {},
  dataById: {},
  notProvidedCounts: {},
  providedCounts: {},
};

const mutations = {
  SET_dataByCols(state, value) {
    state.dataByCols = value;
  },
  SET_dataById(state, value) {
    state.dataById = value;
  },
  SET_notProvidedCounts(state, value) {
    state.notProvidedCounts = value;
  },
  SET_providedCounts(state, value) {
    state.providedCounts = value;
  },
};

const actions = {
  UPDATE_dataByCols({ commit }, payload) {
    commit("SET_dataByCols", payload);
  },
  UPDATE_dataById({ commit }, payload) {
    commit("SET_dataById", payload);
  },
  UPDATE_notProvidedCounts({ commit }, payload) {
    commit("SET_notProvidedCounts", payload);
  },
  UPDATE_providedCounts({ commit }, payload) {
    commit("SET_providedCounts", payload);
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
