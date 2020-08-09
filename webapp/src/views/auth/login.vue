<template>
  <b-container>
    <h1 class="text-center">Log In</h1>
    <b-row class=" d-flex justify-content-center">
      <b-form class="mt-4 col-6 auth-from" id="auth-login">
        <b-form-group label="Email address" label-for="email">
          <b-form-input id="email"
                        size="lg"
                        type="email"
                        required
                        placeholder="Email"/>
        </b-form-group>

        <b-form-group label="Password" label-for="password">
          <b-form-input id="password"
                        size="lg"
                        type="password"
                        required
                        placeholder="Password"/>
        </b-form-group>
        <b-button block size="lg" type="submit" variant="info">Log In</b-button>
        <div class="mt-3 text-center" >
          Don't have an account?
          <b-link title="Log in" to="/user/register">Sign up</b-link>
        </div>
      </b-form>
    </b-row>
  </b-container>
</template>

<script>
  export default {
    name: 'Login',
    components: {},
  };
</script>

<style>
  @import '../../assets/auth.scss';
</style>
