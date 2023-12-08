import React, { memo } from 'react';

import Light403Icon from 'assets/svg/assets-result-403.svg?component';
import Light404Icon from 'assets/svg/assets-result-404.svg?component';
import Light500Icon from 'assets/svg/assets-result-500.svg?component';
import style from './errorPage.module.less';

const ErrorPage: React.FC = () => {
  return (
    <div className={style.errorBox}>
      <Light404Icon />
      <div className={style.title}>404 Not Found</div>
      <div className={style.description}>抱歉，您访问的工单已被删除。</div>
    </div>
  );
};

export default memo(ErrorPage);