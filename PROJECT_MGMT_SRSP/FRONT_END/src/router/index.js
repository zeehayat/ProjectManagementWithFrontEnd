import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/Login.vue';
import Dashboard from '../views/Dashboard.vue';
import RoleList from '../views/RoleList.vue';
import AssignRole from '../views/AssignRole.vue';
import NotificationList from '../views/NotificationList.vue';
import ProjectCreation from '../views/ProjectCreation.vue';
import ProjectAssignment from '../views/ProjectAssignment.vue';
import TaskCreation from '../views/TaskCreation.vue';
import TaskAssignment from '../views/TaskAssignment.vue';
import AddUser from '../views/AddUser.vue';
import TaskUpdate from '@/views/TaskUpdate.vue';
import UserTasks from '@/views/UserTasks.vue';

const routes = [
  { path: '/', name: 'Login', component: Login },
  { path: '/login', name: 'LoginFrm', component: Login },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard, meta: { requiresAuth: true } },
  { path: '/roles', name: 'RoleList', component: RoleList },
  { path: '/assign-role', name: 'AssignRole', component: AssignRole },
  { path: '/notifications', name: 'NotificationList', component: NotificationList },
  { path: '/create-project', name: 'ProjectCreation', component: ProjectCreation },
  { path: '/assign-project', name: 'ProjectAssignment', component: ProjectAssignment },
  {
    path: '/projects/:projectId/create-task',
    name: 'TaskCreation',
    component: TaskCreation,
    props: (route) => ({ projectId: parseInt(route.params.projectId) }),
  },
  { path: '/assign-task', name: 'TaskAssignment', component: TaskAssignment },
  { path: '/add-user', name: 'AddUser', component: AddUser },
  { path: '/tasks', name: 'UserTasks', component: UserTasks, meta: { requiresAuth: true } },
  {
    path: '/tasks/:taskId/update',
    name: 'TaskUpdate',
    component: TaskUpdate,
    props: true,
  },
  {
    path: '/test',
    name: 'TestPage',
    component: () => import('@/views/TestPage.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
