<template>
  <div id="header" class="container mb-5">
      <b-navbar toggleable="lg" variant="default">
        <b-navbar-brand to="/">
          <img alt="logo learn kafka" class="logo" src="./assets/logo.png">
        </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav class="ml-auto">
            <b-nav-item title="Sign up" to="/user/login">Log In</b-nav-item>
            <b-nav-item button title="Register" to="/user/register"><strong>Sign Up</strong>
            </b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    <div id="container">
      <router-view/>
    </div>
  </div>
</template>

<style lang="scss">
  @import 'node_modules/bootstrap/scss/bootstrap';
  @import 'node_modules/bootstrap-vue/src/index.scss';

  .logo {
    max-width: 150px;
  }
</style>
