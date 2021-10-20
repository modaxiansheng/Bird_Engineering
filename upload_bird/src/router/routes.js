import content from '@/components/Content';
import work from '@/components/Work';
const routes = [
  {
    path: '/content',
    name: 'content',
    meta: {
      title: 'content'
    },
    component: content
  },
  {
    path: '/work',
    name: 'work',
    meta: {
      title: 'work'
    },
    component: work
  },
  {
    path: '/',
    redirect: '/content'
  }
];

export default routes;
