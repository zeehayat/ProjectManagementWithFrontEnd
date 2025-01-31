import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/Login.vue';
import Dashboard from '../views/Dashboard.vue';
import RoleList from "../views/RoleList.vue";
import AssignRole from "../views/AssignRole.vue";
import NotificationList from "../views/NotificationList.vue";
import ProjectCreation from "../views/ProjectCreation.vue";
import ProjectAssignment from "../views/ProjectAssignment.vue";
import TaskCreation from "../views/TaskCreation.vue";
import TaskAssignment from "../views/TaskAssignment.vue";

import AddUser from "../views/AddUser.vue";

import TestPage from "../views/TestPage.vue";
import TaskUpdate from "@/views/TaskUpdate.vue";

const routes = [
  { path: '/', name: 'Login', component: Login },

  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
    { path: "/roles", component: RoleList },
  { path: "/assign-role", component: AssignRole },
  { path: "/notifications", component: NotificationList },
    { path: "/create-project", component: ProjectCreation },
  { path: "/assign-project", component: ProjectAssignment },
  { path: "/projects/:projectId/create-task", component: TaskCreation,
    props: (route) => ({ projectId:  parseInt(route.params.projectId) }),
  },
  { path: "/assign-task", component: TaskAssignment },


{ path: '/login', name: 'LoginFrm', component: Login },
    { path: "/add-user", component: AddUser },
    {
  path: "/test",
  component: () => TestPage,
},
    {
  path: '/tasks',
  name: 'UserTasks',
  component: () => import('@/views/UserTasks.vue'),
  meta: { requiresAuth: true },
},
    {
    path: '/tasks/:taskId/update',
    name: 'TaskUpdate',
    component: TaskUpdate,
    props: true,
  },
    {
  path: "/dashboard",
  name: "Dashboard",
  component: () => import("@/views/Dashboard.vue"),
  meta: { requiresAuth: true },
},


];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
console.log(router.getRoutes());