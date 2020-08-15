<template>
  <b-container>
    <h1 class="text-center">Sign up</h1>
    <b-row class=" d-flex justify-content-center">
      <b-form action
              class="mt-4 col-6 auth-from"
              id="auth-register"
              @submit.prevent="createNewUser">
        <b-list-group v-if="errors.length">
          <b-list-group-item variant="danger" v-for="error in errors" v-bind:key="error">
            {{ error }}
          </b-list-group-item>
        </b-list-group>
        <br>
        <b-form-group label="Name" class="text-center" label-for="name">
          <b-form-input
            id="name"
            v-model="name"
            size="lg"
            type="text"
            required
            placeholder="Name"/>
        </b-form-group>

        <b-form-group label="Last name" class="text-center" label-for="last-name">
          <b-form-input id="last-name"
                        size="lg"
                        type="text"
                        v-model="lastName"
                        required
                        placeholder="Last name"/>
        </b-form-group>

        <b-form-group label="Username" label-for="username">
          <b-form-input id="username"
                        size="lg"
                        type="text"
                        required
                        v-model="username"
                        placeholder="Username"/>
        </b-form-group>

        <b-form-group label="Email address" label-for="email">
          <b-form-input id="email"
                        v-model="email"
                        size="lg"
                        type="email"
                        required
                        placeholder="Email"/>
        </b-form-group>

        <b-form-group label="Password" label-for="password">
          <b-form-input id="password"
                        v-model="password"
                        size="lg"
                        type="password"
                        required
                        placeholder="Password"/>

        </b-form-group>
        <b-button block size="lg" type="submit" variant="info">Sign Up</b-button>
        <div class="mt-3 text-center">
          Have an account?
          <b-link title="Log in" to="/user/login">Log in</b-link>
        </div>
      </b-form>
    </b-row>
  </b-container>

</template>

<script>
  export default {
    data: () => ({
      name: "",
      lastName: "",
      username: "",
      email: "",
      password: "",
      errors: []
    }),
    name: 'Register',
    components: {},
    methods: {
      createNewUser() {
        const errors = [];
        const data = JSON.stringify({
          "username": this.username,
          "email": this.email,
          "password": this.password
        });

        const config2 = {
          method: 'post',
          url: 'http://127.0.0.1:8000/api/account/register/',
          headers: {
            'Content-Type': 'application/json'
          },
          data: data
        };
        this.axios(config2)
          .then(function (response) {
            if (response.status) {
              console.log("@TO-DO Manage registered user messages.");
              window.location.href = "/"
            }
          })
          .catch(function (error) {
            if (error.response.status === 409) {
              errors.push("The request could not be completed due to a conflict with the current state of the target resource.")
            }
            console.log("@TO-DO Send the error message to kafka")
          });
        this.errors = errors;
      }
    }
  };
</script>

<style lang="scss">
  @import '../../assets/auth.scss';
</style>
