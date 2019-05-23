<template>
<el-container>
  <el-header>Header</el-header>
  <el-container>
    <el-aside width="200px">Aside</el-aside>
    <el-main>Main</el-main>
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
        password: '',
        cpumem: '',
        diskstorage: '',
        diskstoragetype: 'G',
        note: ''
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
    handleSubDatabase: function () {
      axios.post('/apldb/', {
        dbtype: this.RDSform.dbtype,
        dbstructure: this.RDSform.structure,
        dbname: this.RDSform.dbname,
        username: this.RDSform.username,
        shandow: this.RDSform.password,
        cm: this.RDSform.cpumem,
        disksize: this.RDSform.diskstorage,
        note: this.RDSform.note
      })
    },
    changeFormItem: function () {
     this.RDSform.passsword = 'DBA1后续填写'
    }
  }
}
</script>
<style>
.el-header, .el-footer {
  background-color: #B3C0D1;
  background-height: 200px;
  color: #333;
  text-aligh: center;
  line-height: 60px;
}

.el-aside {
  background-color: #D3DCE6;
  color: #333;
  text-aligh: center;
  line-height: 200px;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  line-height: 160px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}

.el-select .el-input {
  width: 130px;
}
.input-with-select .el-input-group__prepend {
  background-color: #fff;
}
</style>
