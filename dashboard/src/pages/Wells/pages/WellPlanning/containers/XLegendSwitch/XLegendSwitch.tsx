import { Flexbox } from 'components/Box';
import { Switch } from 'antd';
import { useEmissionsTarget } from 'pages/Wells/pages/WellPlanning/containers/EmissionsTargetProvider';
import { Text } from 'components/Typography';
import { useTheme } from 'styled-components';

const XLegendSwitch = () => {
  const { colors } = useTheme();
  const [{ xLegend }, dispatch] = useEmissionsTarget();

  return (
    <Flexbox gap={4} alignItems="center">
      <Text
        color={xLegend === 'days' ? colors.gray['10'] : colors.blue[6]}
        fontSize={8}
      >
        Days
      </Text>

      <Switch
        size="small"
        checked={xLegend === 'dates'}
        onChange={(checked) =>
          dispatch({
            type: 'changeXLegend',
            xLegend: checked ? 'dates' : 'days',
          })
        }
      />

      <Text
        color={xLegend === 'dates' ? colors.gray['10'] : colors.blue[6]}
        fontSize={8}
      >
        Dates
      </Text>
    </Flexbox>
  );
};

export default XLegendSwitch;
