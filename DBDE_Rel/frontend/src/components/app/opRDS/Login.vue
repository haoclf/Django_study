<style lang="less">            
  @import './login.less';      
</style>

<template>
  <div class="login" v-title :data-title="$t('pageTitle.title')">
    <div class="login-con">
      <Card :bordered="false" v-show="loginPage" key="loginCard" class="animated flipInY" :class="{flipOutY:!loginPage}">
        <p slot="title">
          <Icon type="log-in"></Icon>
          {{ $t("login.login") }}
        </p>
        <div class="form-con">
          <Form ref="loginForm" :model="loginForm" :rules="loginFormRule">
            <Form-item prop="username">
              <Input type="text" v-model="loginForm.username" placeholder="Username" @on-enter="handleLoginSubmit()">
                <Icon type="person" slot="prepend"></Icon>
              </Input>
            </Form-item>
            <Form-item prop="password">
              <i class="ivu-icon ivu-input-icon" :class="{'ivu-icon-eye': eyeOpen, 'ivu-icon-eye-disabled': !eyeOpen}" @click="togglePassword"></i>
              <Input :type="inputType" v-model="loginForm.password" placeholder="Password" @on-enter="handleLoginSubmit()">
                <Icon type="locked" slot="prepend"></Icon>
              </Input>
            </Form-item>
            <Form-item>
              <Button @click="handleLoginSubmit" type="primary" long :disabled="loginButtonDisabled">{{ $t("login.login") }}</Button>
            </Form-item>
          </Form>
          <p class="login-tip">
            {{ $t("login.signupTip1") }}
            <a @click="gotoSignup"><u>{{ $t("login.signupTip2") }}</u></a>
            {{ $t("login.signupTip3") }}
          </p>
        </div>
      </Card>
      <Card :bordered="false" v-show="!loginPage" key="signupCard" class="animated flipInY" :class="{flipOutY:loginPage}">
        <p slot="title">
          <Icon type="person-add"></Icon>
          {{ $t("login.signup") }}
        </p>
        <div class="form-con">
          <Form ref="signupForm" :model="signupForm" :rules="signupFormRule" :label-width="70">
            <Form-item prop="username" :label="$t('login.username')">
              <Input type="text" v-model="signupForm.username" placeholder="Username" @on-enter="handleSignupSubmit()">
                <Icon type="person" slot="prepend"></Icon>
              </Input>
            </Form-item>
            <Form-item prop="email" :label="$t('login.email')">
              <Input type="text" v-model="signupForm.email" placeholder="Email" @on-enter="handleSignupSubmit()">
                <Icon type="email" slot="prepend"></Icon>
              </Input>
            </Form-item>
            <Form-item prop="password1" :label="$t('login.password')">
              <i class="ivu-icon ivu-input-icon" :class="{'ivu-icon-eye': eyeOpen1, 'ivu-icon-eye-disabled': !eyeOpen1}" @click="togglePassword1"></i>
              <Input :type="inputType1" v-model="signupForm.password1" placeholder="Password" @on-enter="handleSignupSubmit()">
                <Icon type="locked" slot="prepend"></Icon>
              </Input>
            </Form-item>
            <Form-item prop="password2" :label="$t('login.passwordConfirm')">
              <i class="ivu-icon ivu-input-icon" :class="{'ivu-icon-eye': eyeOpen2, 'ivu-icon-eye-disabled': !eyeOpen2}" @click="togglePassword2"></i>
              <Input :type="inputType2" v-model="signupForm.password2" placeholder="Password" @on-enter="handleSignupSubmit()">
                <Icon type="locked" slot="prepend"></Icon>
              </Input>
            </Form-item>
          </Form>
          <div style="text-align:center">
            <Button size="small" icon="arrow-return-left" @click="backtoLogin()">{{ $t("common.goback") }}</Button>
            <Button size="small" icon="checkmark-round" type="primary" @click="handleSignupSubmit()" style="margin-left: 20px">{{ $t("login.signup") }}</Button>
          </div>
        </div>
      </Card>
    </div>
  </div>
</template>

<script>
import axios from '@/axios'
import {router} from '@/router'

export default {
  name: 'Login',
  data () {
    return {
      loginPage: true,
      loginForm: {
        username: '',
        password: ''
      },
      loginFormRule: {
        username: [
          {
            required: true,
            message: this.$t('login.enterUsername'),
            trigger: 'blur'
          }
        ],
        password: [
          {
            required: true,
            message: this.$t('login.enterPassword'),
            trigger: 'blur'
          },
          {
            type: 'string',
            min: 6,
            message: this.$t('login.passwordLenError'),
            trigger: 'blur'
          }
        ]
      },
      signupForm: {
        username: '',
        email: '',
        password1: '',
        password2: ''
      },
      signupFormRule: {
        username: [
          {
            required: true,
            validator: this.validateUsername,
            trigger: 'blur'
          }
        ],
        email: [
          {
            required: true,
            message: this.$t('login.enterEmail'),
            trigger: 'blur'
          },
          {
            type: 'email',
            message: this.$t('login.emailFormatInvalid'),
            trigger: 'blur'
          }
        ],
        password1: [
          {
            required: true,
            message: this.$t('login.enterPassword'),
            trigger: 'blur'
          },
          {
            type: 'string',
            min: 6,
            message: this.$t('login.passwordLenError'),
            trigger: 'blur'
          }
        ],
        password2: [
          {
            required: true,
            validator: this.validatePassword,
            trigger: 'blur'
          }
        ]
      },
      eyeOpen: true,
      eyeOpen1: true,
      eyeOpen2: true,
      inputType: 'password',
      inputType1: 'password',
      inputType2: 'password'
    }
  },
  methods: {
    gotoSignup () {
      this.eyeOpen1 = true
      this.eyeOpen2 = true
      this.inputType1 = 'password'
      this.inputType2 = 'password'
      this.$refs.signupForm.resetFields()
      this.loginPage = false
    },
    backtoLogin () {
      this.eyeOpen = true
      this.inputType = 'password'
      this.$refs.loginForm.resetFields()
      this.loginPage = true
    },
    handleLoginSubmit () {
      axios.post('/tokens/', this.loginForm).then((response) => {
        this.$store.dispatch('storeToken', response.data.token)
        this.$store.dispatch('storeUsername', this.loginForm.username)
        router.push({name: 'Overview'})
      }, (response) => {
        this.$Message.error(this.$t('login.loginFailed'))
      })
    },
    togglePassword () {
      this.eyeOpen = !this.eyeOpen
      if (this.eyeOpen) {
        this.inputType = 'password'
      } else {
        this.inputType = 'text'
      }
    },
    handleSignupSubmit () {
      this.$refs.signupForm.validate((valid) => {
        if (!valid) {
          this.$Message.error(this.$t('rule.formValidateFailed'))
        } else {
          axios.post('/signup/', {
            username: this.signupForm.username,
            password: this.signupForm.password1,
            email: this.signupForm.email
          }).then((response) => {
            this.$refs.signupForm.resetFields()
            this.$Message.success({
              content: this.$t('login.signupSuccess'),
              duration: 3
            })
            setTimeout(() => {
              this.backtoLogin()
            }, 2000)
          }, (response) => {
            this.$Message.error(this.$t('login.signupError'))
          })
        }
      })
    },
    togglePassword1 () {
      this.eyeOpen1 = !this.eyeOpen1
      if (this.eyeOpen1) {
        this.inputType1 = 'password'
      } else {
        this.inputType1 = 'text'
      }
    },
    togglePassword2 () {
      this.eyeOpen2 = !this.eyeOpen2
      if (this.eyeOpen2) {
        this.inputType2 = 'password'
      } else {
        this.inputType2 = 'text'
      }
    },
    validateUsername (rule, value, callback) {
      if (!value) {
        callback(new Error(this.$t('login.enterUsername')))
      }
      callback()
    },
    validatePassword (rule, value, callback) {
      if (!value) {
        callback(new Error(this.$t('rule.notEmpty')))
      } else if (value !== this.signupForm.password1) {
        callback(new Error(this.$t('rule.passwordNotSame')))
      }
      callback()
    }
  },
  computed: {
    loginButtonDisabled () {
      return (this.loginForm.username.length === 0 ||
              this.loginForm.password.length < 6)
    }
  }
}
</script>
