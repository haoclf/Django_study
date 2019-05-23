<template>
  <div class='all-login' style="height: 100%">
    <div id='login-id' class='login-cla' v-show='eyes.eyeopenLogin'>
      <!-- <h1 class="DBDElogo">DBDE | 数据库平台</h1> -->
      <el-form id="logging-form-login" :model="ruleForm2" size="small" status-icon :rules="rules2" ref="ruleForm2" lable-position="right" label-width="1300px" class="demo-ruleForm">
      <el-row type="flex" justify="center" align="middle">
        <el-col :span="50">
        <h3>{{ $t("login.userlogin") }}</h3>
        <el-form-item :label="$t('login.username')" prop="user">
          <!-- <el-input  :placeholder="$t('login.enterUsername')"  v-model="ruleForm2.name" clearable></el-input> -->
          <el-input  :placeholder="$t('login.enterUsername')"  v-model="loginForm.username" clearable></el-input>
        </el-form-item>
        <el-form-item :label="$t('login.password')" prop="pass">
          <!-- <el-input type="password" :placeholder="$t('login.enterPassword')" v-model="ruleForm2.pass" autocomplete="off"></el-input>  -->
          <el-input type="password" :placeholder="$t('login.enterPassword')" v-model="loginForm.password" autocomplete="off"></el-input>
        </el-form-item>
        <!-- <el-form-item :label="$t("login.passwordConfirm")" prop="checkPass">
          <el-input type="password" v-model="ruleForm2.checkPass" autocomplete="off"></el-input>
        </el-form-item>  -->
        <el-form-item label-position="left" lable-width="100px">
          <!-- <el-button ref="login" type="primary" @click="submitForm('ruleForm2')">{{ $t("login.login") }}</el-button> -->
          <el-button ref="login" type="primary" @click="handleLoginSubmit">{{ $t("login.login") }}</el-button>
          <el-button @click="jumpToRegister('register')">{{ $t("login.signup") }}</el-button>
        </el-form-item>
        </el-col>
      </el-row>
      </el-form>
    </div>
    <div id='login-id' class='login-cla' v-show='!eyes.eyeopenLogin'>
          <!-- <h1 class="DBDElogo">DBDE | 数据库平台</h1> -->
          <el-form id="logging-form-register" :model="registerForm" size="small" status-icon :rules="registerRule" ref="registerForm" lable-position="right" label-width="1300px" class="demo-ruleForm">
          <el-row type="flex" justify="center" align="middle">
            <el-col :span="50">
            <h3>用户注册</h3>
            <el-form-item label="用户" prop="user">
              <el-input  placeholder="请输入帐号"  v-model="registerForm.username" clearable></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password1">
              <el-input type="password" placeholder="请输入密码" v-model="registerForm.password1" autocomplete="off"></el-input>
            </el-form-item>
             <el-form-item label="确认密码" prop="password2">
              <el-input type="password" v-model="registerForm.password2" placeholder="请输入密码" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label-position="left" lable-width="100px">
              <el-button ref="register" type='primary' @click="handleSignupSubmit()">注册</el-button>
              <el-button @click="resetForm('ruleForm2')">清空填写内容</el-button>
              <el-button @click="jumpToRegister('login')">返回登录</el-button>
            </el-form-item>
            </el-col>
          </el-row>
          </el-form>
        </div>
</div>
</template>

<script>
import axios from '@/axios'
import {store} from '@/store'

export default {
  data () {
    var checkAge = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('年龄不能为空'))
      }
      setTimeout(() => {
        if (!Number.isInteger(value)) {
          callback(new Error('请输入数字值'))
        } else {
          if (value < 18) {
            callback(new Error('必须年满18岁'))
          } else {
            callback()
          }
        }
      }, 1000)
    }
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.ruleForm2.checkPass !== '') {
          this.$refs.ruleForm2.validateField('checkPass')
        }
        callback()
      }
    }
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.ruleForm2.pass) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    var validateregisterPass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.registerForm.password2 !== '') {
          this.$refs.registerForm.validateField('password2')
        }
        callback()
      }
    }
    var validateregisterPass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.registerForm.password1) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      ruleForm2: {
        name: '',
        pass: '',
        checkPass: '',
        age: ''
      },
      rules2: {
        pass: [
          { validator: validatePass, trigger: 'blur' }
        ],
        checkPass: [
          { validator: validatePass2, trigger: 'blur' }
        ],
        age: [
          { validator: checkAge, trigger: 'blur' }
        ]
      },
      registerRule: {
       password1: [
         { validator: validateregisterPass, trigger: 'blur' }
       ],
       password2: [
         { validator: validateregisterPass2, trigger: 'blur' }
       ],
       email: [
         { validator: checkAge, trigger: 'blur' }
       ]
      },     eyes: {
        eyeopenLogin: true,
        eyeopenRegister: false
      },
      loginForm: {
        'username': '',
        'password': ''
      },
      registerForm: {
        username: '',
        email: 'aa',
        password1: '',
        password2: ''
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!')
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    jumpToRegister: function (e) {
      if (e === 'login') {
        this.eyes.eyeopenLogin = true
      } else {
        this.eyes.eyeopenLogin = false
      }
    },
    handleLoginSubmit: function () {
        axios.post('/jwt-token/', this.loginForm).then((response) => {
        this.$store.dispatch('storeToken', response.data.token)
        this.$store.dispatch('storeUsername', this.loginForm.username)
        this.$router.push({name: 'HomeLink'})
      }, (response) => {
        this.$Message.error(this.$t('login.loginFailed'))
      }) 
    },
    handleSignupSubmit () {
      console.log('startSignup')
      console.log(this.registerForm)
      this.$refs.registerForm.validate((valid) => {
        if (!valid) {
          console.log('1')
          this.$Message.error(this.$t('rule.formValidateFailed'))
        } else {
          console.log('2')
          axios.post('/register/', {
            username: this.registerForm.username,
            password: this.registerForm.password1,
            password2: this.registerForm.password2,
          }).then((response) => {
            console.log('3')
            console.log(response)
            this.$refs.registerForm.resetFields()
            this.$notify({
              title: this.$t('login.signupSuccess'),
              message: '注册用户' + response.data.username,
              type: 'success'
            })
            setTimeout(() => {
              this.backtoLogin()
            }, 2000)
          }, (response) => {
            this.$notify.error({
              title: this.$t('login.signupError'),
              message: '注册用户' + response.data.username
            })
          })
        }
      })
    }
  }
}
</script>

<style scoped>
.all-login {
  width: 100%;
  heigth: 100%;
  background-image: url('../../assets/login_bg.jpg');
  background-position: top;
  background-size: 1900px 1000px;
  position: fixed;
  margin: 0px 0px 0px 0px;
}

#login-id {
  width: 95%;
  heigth: 95%;
  top: 60%;
}

#logging-form-login {
  heigth: 95%;
  top: 60%;
  margin-top: 370px;
  margin-left: 0px;
  text-color: green;
  color: #606266;
}
#logging-form-register {
  heigth: 95%;
  top: 60%;
  margin-top: 370px;
  margin-left: 0px;
  text-color: green;
  color: #606266;
}
h3 {
  text-align: right;
  width: 88%;
  font-color: white;
}
.DBDElogo {
  position: absolute;
  top: 150px;
  left: 130px;
  width: 400px;
  height: 100%;
  color: #C0C4CC;
}
</style>
