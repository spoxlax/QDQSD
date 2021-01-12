import React from 'react';
import { Row, Col } from 'antd';
import { withTranslation } from 'react-i18next';
import { Fade } from 'react-reveal';
import loadable from '@loadable/component';

import * as S from './styles';

const Button = loadable(() => import('../../common/Button'));

const MiddleBlock = ({ title, content, button, t }) => {
  return (
    <S.MiddleBlock>
      <Row type="flex" justify="center" align="middle">
        <Fade bottom>
          <S.ContentWrapper>
            <Col lg={24} md={24} sm={24} xs={24}>
              <h6>{t(title)}</h6>
              <S.Content>{t(content)}</S.Content>
              {button ? (
                <Button name="submit" type="submit">
                  {t(button)}
                </Button>
              ) : (
                ''
              )}
            </Col>
          </S.ContentWrapper>
        </Fade>
      </Row>
    </S.MiddleBlock>
  );
};

export default withTranslation()(MiddleBlock);
