import React, { memo } from 'react';
import Style from './Menu.module.less';
import FullLogo from 'assets/svg/assets-logo-full.svg?component';
import MiniLogo from 'assets/svg/assets-t-logo.svg?component';
import { useNavigate } from 'react-router-dom';

interface IProps {
  collapsed?: boolean;
}

export default memo((props: IProps) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate('/');
  };

  return (
    <div style={{fontStyle: 'italic',fontWeight:'bold',fontSize:'25px'}} className={Style.menuLogo} onClick={handleClick}>
      工单系统
      {/* {props.collapsed ? <MiniLogo /> : <FullLogo />} */}
    </div>
  );
});
