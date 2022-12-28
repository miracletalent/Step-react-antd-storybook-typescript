import ChartYScaleProvider from 'pages/Wells/containers/ChartYScaleProvider';
import EmissionsTargetProvider, {
  EmissionsTargetValue,
  useEmissionsTarget,
} from 'pages/Wells/pages/WellPlanning/containers/EmissionsTargetProvider';
import { Title, Text } from 'components/Typography';
import Box, { Flexbox } from 'components/Box';
import { InfoCircleOutlined } from '@ant-design/icons';
import TotalCO2EmissionsTarget from 'pages/Wells/pages/WellPlanning/containers/TotalCO2EmissionsTarget';
import EmissionsTargetSwitch from 'pages/Wells/pages/WellPlanning/containers/EmissionsTargetSwitch';
import CO2EmissionsTargetChart from 'pages/Wells/pages/WellPlanning/containers/CO2EmissionsTargetChart';
import EmissionsTargetFilters from 'pages/Wells/pages/WellPlanning/containers/EmissionsTargetFilters';
import XLegendSwitch from 'pages/Wells/pages/WellPlanning/containers/XLegendSwitch';
import { useTheme } from 'styled-components';
import { useChartYScale } from 'pages/Wells/containers/ChartYScaleProvider';
import EmissionsTimelines from '../EmissionsTimelines';

const EmissionsTarget = () => {
  const [{ value }] = useEmissionsTarget();
  const { colors } = useTheme();
  const { yScalesWidths } = useChartYScale();
  const marginLeft = yScalesWidths['y'] || 0;
  return (
    <>
      <Flexbox justifyContent="space-between">
        <Box marginTop={30}>
          <Flexbox alignItems="center">
            <Title level={4}>Emissions target</Title>
            <Box marginLeft={6}>
              <Text fontSize={16}>
                <InfoCircleOutlined />
              </Text>
            </Box>
          </Flexbox>
          <Box marginTop={10}>
            <EmissionsTargetSwitch />
          </Box>
        </Box>
        {value === EmissionsTargetValue.CO2 ? (
          <TotalCO2EmissionsTarget />
        ) : null}
      </Flexbox>
      <Box marginTop={16}>
        <EmissionsTargetFilters />
      </Box>
      <Box marginTop={14}>
        {value === EmissionsTargetValue.CO2 ? (
          <CO2EmissionsTargetChart />
        ) : null}
      </Box>
      <Flexbox alignItems="center" marginTop={6} marginLeft={marginLeft}>
        <Flexbox flexShrink={0}>
          <XLegendSwitch />
        </Flexbox>
        <Flexbox justifyContent="center" flexGrow={1}>
          <Text color={colors.gray['10']}>Target daily emissions</Text>
        </Flexbox>
      </Flexbox>
      <Box marginTop={18} marginLeft={marginLeft}>
        <EmissionsTimelines />
      </Box>
    </>
  );
};

const DefaultEmissionsTarget = () => {
  return (
    <ChartYScaleProvider>
      <EmissionsTargetProvider>
        <EmissionsTarget />
      </EmissionsTargetProvider>
    </ChartYScaleProvider>
  );
};

export default DefaultEmissionsTarget;
