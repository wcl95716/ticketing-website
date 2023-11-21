import React, { memo } from 'react';
import { useNavigate } from 'react-router-dom';
import { Popup, Badge, Dropdown, Space } from 'tdesign-react';
import {
  Row, Col,
  Breadcrumb, Layout, Menu, theme, Table, Form, Input, Button, Select, DatePicker
} from "antd";
import { getTicketListRequest, getAllUserRequest, getUserDetail, updateTicket, selecAllUser } from 'models/ticketing-website/index.model';
import {
  Icon,
  LogoGithubIcon,
  MailIcon,
  HelpCircleIcon,
  SettingIcon,
  PoweroffIcon,
  UserCircleIcon,
} from 'tdesign-icons-react';
import { useAppDispatch, useAppSelector } from 'modules/store';
import { toggleSetting } from 'modules/global';
import { logout } from 'modules/user';
import Style from './HeaderIcon.module.less';

const { DropdownMenu, DropdownItem } = Dropdown;

export default memo(() => {
  const dispatch = useAppDispatch();
  const navigate = useNavigate();
  const allUserList = useAppSelector(selecAllUser);
  const userOption = [];
  allUserList.forEach((item) => {
    userOption.push({
      label: item?.name,
      value: item?.user_id
    })
  })

  const gotoWiki = () => {
    window.open('https://tdesign.tencent.com/react/overview');
  };

  const gotoGitHub = () => {
    window.open('https://github.com/Tencent/tdesign-react-starter');
  };

  const clickHandler = (data: any) => {
    if (data.value === 1) {
      navigate('/user/index');
    }
  };
  const handleLogout = async () => {
    await dispatch(logout());
    navigate('/login/index');
  };

  const filterOption = (input: string, option?: { label: string; value: string }) =>
    (option?.label ?? '').toLowerCase().includes(input.toLowerCase());


  const onUserChange = (value) => {
    // console.log("登陆人value",value)
    dispatch(getUserDetail(value));
  }


  return (
    <Space align='center'>
      {/* <Badge className={Style.badge} count={6} dot={false} maxCount={99} shape='circle' showZero={false} size='medium'>
        <Button className={Style.menuIcon} shape='square' size='large' variant='text' icon={<MailIcon />} />
      </Badge> */}
      {/* <Popup content='代码仓库' placement='bottom' showArrow destroyOnClose>
        <Button
          className={Style.menuIcon}
          shape='square'
          size='large'
          variant='text'
          onClick={gotoGitHub}
          icon={<LogoGithubIcon />}
        />
      </Popup>
      <Popup content='帮助文档' placement='bottom' showArrow destroyOnClose>
        <Button
          className={Style.menuIcon}
          shape='square'
          size='large'
          variant='text'
          onClick={gotoWiki}
          icon={<HelpCircleIcon />}
        />
      </Popup> */}

      <Select style={{ width: 120 }} placeholder="登陆人" allowClear showSearch filterOption={filterOption}
        options={userOption} onChange={onUserChange}
      ></Select>
      {/* <Dropdown trigger={'click'} onClick={clickHandler}>

        <Button variant='text' className={Style.dropdown}>
          <Icon name='user-circle' className={Style.icon} />
          <span className={Style.text}>Tencent</span>
          <Icon name='chevron-down' className={Style.icon} />
        </Button>
        <DropdownMenu>
          <DropdownItem value={1}>
            <div className={Style.dropItem}>
              <UserCircleIcon />
              <span>个人中心</span>
            </div>
          </DropdownItem>
          <DropdownItem value={1} onClick={handleLogout}>
            <div className={Style.dropItem}>
              <PoweroffIcon />
              <span>退出登录</span>
            </div>
          </DropdownItem>
        </DropdownMenu>
      </Dropdown> */}
      {/* <Popup content='页面设置' placement='bottom' showArrow destroyOnClose>
        <Button
          className={Style.menuIcon}
          shape='square'
          size='large'
          variant='text'
          onClick={() => dispatch(toggleSetting())}
          icon={<SettingIcon />}
        />
      </Popup> */}
    </Space>
  );
});
