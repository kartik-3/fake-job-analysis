const state = {
  user_chat: [],
};

const mutations = {
  SET_USER_CHAT(state, value) {
    state.user_chat.push({
      from: "user",
      msg: value,
    });
  },
  SET_BOT_CHAT(state, value) {
    state.user_chat.push({
      from: "bot",
      msg: value,
    });
  },
};

const actions = {
  updateUserChat({ commit }, payload) {
    commit("SET_USER_CHAT", payload);
  },
  updateBotChat({ commit }, payload) {
    commit("SET_BOT_CHAT", payload);
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
