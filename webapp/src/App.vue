<template>
  <div id="app">
    <b-navbar toggleable="lg"  variant="default">
    <b-navbar-brand to="/">
      <img alt="logo learn kafka" class="logo" src="./assets/logo.png">
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/">Home</b-nav-item>
        <b-nav-item to="/about">About</b-nav-item>

      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
    <router-view/>
  </div>
</template>

<style lang="scss">
@import 'node_modules/bootstrap/scss/bootstrap';
@import 'node_modules/bootstrap-vue/src/index.scss';
.logo {
  max-width: 150px;
}
</style>
