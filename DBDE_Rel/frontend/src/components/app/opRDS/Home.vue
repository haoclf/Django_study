<template>
<el-container>
  <el-aside width="200px">
    <div id="Home-side-div">
<el-row class="tac">
  <el-col :span="24">
    <h5>智融集团 | DBDE平台</h5>
    <!-- <el-menu default-active="2" text-color="#409EFF" background-color="#303133" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose"> -->
    <el-menu :default-active="$route.path" router unique-opened width="1200px"  class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose">
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span width="1200px">资源管理</span>
        </template>
        <el-menu-item-group>
          <template slot="title">RDS</template>
          <el-menu-item index="/mysqlResource">MySQL</el-menu-item>
          <el-menu-item index="/home/postgresql">PostgreSQL</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="内存数据库">
          <el-menu-item index="1-3">Online</el-menu-item>
        </el-menu-item-group>
        <el-submenu index="1-4">
          <template slot="title">Redis</template>
          <el-menu-item index="1-4-1">选项1</el-menu-item>
        </el-submenu>
        <el-submenu index="1-4">
          <template slot="title">Memcache</template>
          <el-menu-item index="1-4-1">选项1</el-menu-item>
        </el-submenu>
      </el-submenu>
      <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title">服务管理</span>
      </el-menu-item>
      <el-menu-item index="3" disabled>
        <i class="el-icon-document"></i>
        <span slot="title">后台管理</span>
      </el-menu-item>
      <el-menu-item index="4">
        <i class="el-icon-setting"></i>
        <router-link :to="{name: 'settingLink'}" >配置</router-link>
      </el-menu-item>
      <el-submenu index="5">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span width="1200px">管理</span>
        </template>
        <el-menu-item-group>
          <template slot="title">RDS</template>
          <el-menu-item index="1-1">MySQL</el-menu-item>
          <el-menu-item index="1-2">PostgreSQL</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="内存数据库">
          <el-menu-item index="1-3">Online</el-menu-item>
        </el-menu-item-group>
        <el-submenu index="1-4">
          <template slot="title">Redis</template>
          <el-menu-item index="1-4-1">选项1</el-menu-item>
        </el-submenu>
        <el-submenu index="1-4">
          <template slot="title">Memcache</template>
          <el-menu-item index="1-4-1">选项1</el-menu-item>
        </el-submenu>
      </el-submenu>

    </el-menu>
  </el-col>
  <el-col :span="12">
  </el-col>
</el-row>
</div>
  </el-aside>
  <el-container>
    <el-header>
      <div id="Home-headr-div">
      <el-row :gutter="20" type="flex" class="row-bg" justify="end">
      <el-col :offset="16">
      <div class="grid-content bg-purple">
<el-menu id="elMenuHeader" :default-active="activeIndex" class="el-menu-demo" mode="horizontal" menu-trigger="click" @select="handleSelect">
  <el-menu-item index="1">运行状态</el-menu-item>
  <el-submenu index="2">
    <template slot="title">changhao</template>
    <el-menu-item index="2-1">个人信息</el-menu-item>
    <el-menu-item index="2-2">修改密码</el-menu-item>
    <el-menu-item index="2-3">注销</el-menu-item>
    <el-submenu index="2-4">
      <template slot="title">选项4</template>
      <el-menu-item index="2-4-1">选项1</el-menu-item>
      <el-menu-item index="2-4-2">选项2</el-menu-item>
      <el-menu-item index="2-4-3">选项3</el-menu-item>
    </el-submenu>
  </el-submenu>
  <el-menu-item index="3" disabled>消息中心</el-menu-item>
  <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">联系我们</a><!-- <router-link to="name: ele.me" target="_blank">联系我们</router-link> --></el-menu-item>
</el-menu>
   </div>
   </el-col>
   </el-row>
</div>
    </el-header>
    <el-main>
    <router-view></router-view>
    <el-col>
      <el-row><el-button type="primary" @click="celeryTask()" >申请资源</el-button><el-button icon="el-icon-delete" type="danger" @click="alertLog()">释放资源</el-button><el-button icon="el-icon-rank" type="primary" size="small" @click="jump()">查看资源</el-button></el-row>
    </el-col>
      <img src="@/assets/佟丽娅2.jpg" height='746' width='569'>
      <img src="@/assets/vue-study1.png" height='746' width='569'>
      <img v-bind:src="picPath">
      <br>
      <el-button type="primary" @click="dialogFormVisible = true">申请数据库</el-button>
      <el-dialog title="申请数据库" :visible.sync="dialogFormVisible" :append-to-body="true" width="45%" @click="changeFormItem()">
        <el-form :model="RDSform" :inline="true" class="demo-form-inline">
          <el-row :gutter="20">
            <el-col :span="12">
              <el-form-item label="数据库类型:" :label-width="formLabelWidth">
                <el-select v-model="RDSform.dbtype" placeholder="可选择类型" @change="changeRegion()">
                  <el-option label="MySQL" value="MySQL"></el-option>
                  <el-option label="Redis" value="Redis"></el-option>
                  <el-option label="Memcache" value="Memcache"></el-option>
                  <el-option label="PostgreSQL" value="PostgreSQL"></el-option>
                </el-select>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="架构类型:" :label-width="formLabelWidth">
              <el-select v-model="RDSform.structure" placeholder="可选择类型">
                <el-option label="单实例" value="single"></el-option>
                <el-option label="主从结构" value="ms"></el-option>
              </el-select>
            </el-form-item>
            </el-col>
          </el-row>          
          <el-row :gutter="50">
            <el-col :span="12">
              <el-form-item label="用户名(DB):">
                <el-input v-model="RDSform.username" style="width:250px" type="text"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="密码:">
                <el-input v-model="RDSform.password" :disabled="true" placeholder="DBA后续填写"  style="width:270px"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span=24 style="height: 55px;width: 100px;" size="medium">
              <el-radio-group v-model="RDSform.onlyReadUser">
                <el-radio @click.native.prevent="clickReadOnlyUser()" label="1" border>是否需要只读用户</el-radio>
              </el-radio-group>
            </el-col>
          </el-row>
          <el-row>
          <el-col>
            <el-form-item label="数据库名称" :label-width="formLabelWidth" class="demo-input-suffix">
              <el-input v-model="RDSform.dbname" autocomplete="off" style="width:650px" placeholder="部门-库名"><template slot="prepend">{{ RDSform.typename  }}</template></el-input>
              <p>数据库名称格式: {{ RDSform.typename  }}部门-库名</p>
            </el-form-item>
          </el-col>
          </el-row>
          <div style="margin-top: 15px;">
          <el-row :gutter="20">
            <el-col :span="12">
              <el-form-item label="CPU/Mem:" :label-width="formLabelWidth">
                <el-select v-model="RDSform.cpumem" placeholder="可选择类型" @change="changeRegion()">
                  <el-option label="1核2G" value="c1m2"></el-option>
                  <el-option label="2核4G" value="c2m4"></el-option>
                  <el-option label="4核4G" value="c4m4"></el-option>
                  <el-option label="4核8G" value="c4m8"></el-option>
                </el-select>
                <!-- <p>{{ RDSform.typename }}  {{ RDSform.region }}</p>  -->
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="磁盘容量">
                <el-input v-model="RDSform.diskstorage" style="width:200px" type="text" class="input-with-select">
                  <el-select v-model="RDSform.diskstoragetype" slot="append" style="width:50px" placeholder="G">
                    <el-option label="G" value="G"></el-option>
                    <el-option label="M" value="M"></el-option>
                    <el-option label="T" value="T"></el-option>
                  </el-select>
                </el-input>
              </el-form-item>
            </el-col>
          </el-row>
          </div>
          <el-row>
            <el-col :span="12">
              <el-form-item label="备注(DB):">
              <el-input
                type="textarea"
                :autosize="{ minRows: 2, maxRows: 4}"
                placeholder="数据库用途,直接使用人"
                v-model="RDSform.note" style="width: 250px;">
              </el-input>
              </el-form-item>
            </el-col>
          </el-row>
          </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogFormVisible = false;handleSubDatabase()">确 定</el-button>
        </div>
      </el-dialog>
      <div>
        <router-view></router-view>
      </div>
    </el-main>
    <el-footer>
      <el-row>
      <el-col :span="6" :offset="16">
      <el-button-group>
        <el-button type="primary" icon="el-icon-arrow-left">上一页</el-button>
        <el-button type="primary">下一页<i class="el-icon-arrow-right el-icon--right"></i></el-button>
      </el-button-group>
      </el-col>
      </el-row>
      Copyright: 2019
    </el-footer>
  </el-container>
</el-container>
</template>

<script>
import axios from '@/axios'
import {store} from '@/store'

export default {
  name: 'opRDSHome',
  data () {
    return {
      name: 'haoc',
      picPath: '@/assets/dota2.jpg',
      dialogFormVisible: false,
      activeIndex: '1',
      formLabelWidth: "10",
      RDSform: {
        dbname: '',
        typename: 'mysql-BJ-',
        dbtype: '',
        type: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        resource: '',
        desc: '',
        structure: '',
        username: '',
        password: 'DBAShadown',
        cpumem: '',
        diskstorage: '',
        diskstoragetype: 'G',
        note: '',
        onlyReadUser: '0'
      }
    }
  },
  methods: {
    alertLog: function () {
      console.log('success!')
      alert('success!')
    },
    jump: function () {
      // this.$router.go(-1)
      // this.$router.replace("/")
      // this.$router.replace({name: 'resourceLink'})
      this.$router.push({name: 'resourceLink'})
    },
    handleOpen: function (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose: function (key, keyPath) {
      console.log(key, keyPath)
    },
    handleSelect: function (key, keyPath) {
      console.log(key, keyPath)
    },
    changeRegion: function () {
      if (this.RDSform.dbtype == 'MySQL') {
          this.RDSform.typename = 'mysql-BJ-'
      } else if (this.RDSform.dbtype == 'PostgreSQL') {
          this.RDSform.typename = 'pg-BJ-'
      } else if (this.RDSform.dbtype == 'Redis') {
          this.RDSform.typename = 'redis-BJ-'
      } else if (this.RDSform.dbtype == 'Memcache') {
          this.RDSform.typename = 'memcache-BJ-'
      }
    },
    clickReadOnlyUser: function (e) {
      e === this.RDSform.onlyReadUser ? this.RDSform.onlyReadUser = '' : this.RDSform.onlyReadUser = e
    },
    handleSubDatabase: function () {
      // axios.post('/apldb/', {
      axios.post('/celerytask/', {
        dbtype: this.RDSform.dbtype,
        dbstructure: this.RDSform.structure,
        dbname: this.RDSform.dbname,
        username: this.RDSform.username,
        shandow: this.RDSform.password,
        cm: this.RDSform.cpumem,
        disksize: this.RDSform.diskstorage,
        note: this.RDSform.note
      }).then((response) => {
        alert('lk')
        console.log(response)
        console.log(response.data)
        console.log(response.status)
        if (response.status === 201) {
          this.$notify({
            title: '成功',
            message: '数据库申请已提交',
            type: 'success'
          })
          this.$notify.close()
        } else {
          this.$notify({
            title: '警告',
            message: '数据库申请提交失败',
            type: 'warning'
          })
          this.$notify.close()
        }
      }).catch((response) => {
        console.log(response.data)
          this.$notify({
            title: '警告',
            message: '数据库申请提交失败,错误码:' + response.status,
            type: 'warning'
          })
       })
        },
    celeryTask: function () {
       axios.post('/celerytask/', {
         key: 'test' 
      }).then(function (response) {
       console.log('e')
      }).catch(function (error) {
        alert(error);
      })
    }
    },
    changeFormItem: function () {
     this.RDSform.passsword = 'DBA1后续填写'
    }
}
</script>
<style>
.el-select .el-input {
  width: 130px;
}
.input-with-select .el-input-group__prepend {
  background-color: #fff;
}
</style>
