<template>
  <b-container>
    <h1 class="text-center">Sign up</h1>
    <b-row class=" d-flex justify-content-center">
      <b-form class="mt-4 col-6 auth-from" id="auth-register">
        <b-form-group label="Name" class="text-center" label-for="name">
          <b-form-input id="name" size="lg" type="text" required placeholder="Name"/>
        </b-form-group>

        <b-form-group label="Last name" class="text-center" label-for="last-name">
          <b-form-input id="last-name"
                        size="lg"
                        type="text"
                        required
                        placeholder="Last name"/>
        </b-form-group>

        <b-form-group label="Username" label-for="username">
          <b-form-input id="username" size="lg" type="text" required placeholder="Enter username"/>
        </b-form-group>

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
         <b-form-group label="Password" label-for="password_2">
          <b-form-input id="password_2"
                        size="lg"
                        type="password"
                        required
                        placeholder="Repeat password"/>
        </b-form-group>
        <b-button block size="lg" type="submit" variant="info">Sign Up</b-button>
        <div class="mt-3 text-center" >
          Have an account?
          <b-link title="Log in" to="/user/login">Log in</b-link>
        </div>
      </b-form>
    </b-row>

  </b-container>

</template>

<script>
  export default {
    name: 'Register',
    components: {},
  };
</script>

<style lang="scss">
  @import '../../assets/auth.scss';
</style>
