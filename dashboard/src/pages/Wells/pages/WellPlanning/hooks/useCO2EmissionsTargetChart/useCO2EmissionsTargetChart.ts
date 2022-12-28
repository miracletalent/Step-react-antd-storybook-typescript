import { ChartDataset } from 'chart.js';
import { useMemo } from 'react';
import useBaselineCO2Emissions from 'pages/Wells/pages/WellPlanning/hooks/useBaselineCO2Emissions';
import useTargetCO2Emissions from 'pages/Wells/pages/WellPlanning/hooks/useTargetCO2Emissions';
import useCurrentWellPlan from 'pages/WellPlan/hooks/useCurrentWellPlan';
import { useEmissionsTarget } from '../../containers/EmissionsTargetProvider';
import { useTheme } from 'styled-components';
import { notEmpty } from 'utils/data';
import parseISO from 'date-fns/parseISO';
import format from 'date-fns/format';
import { DATE_FORMAT_SHORT } from 'consts';
import { calculateTotalCO2Emission } from 'pages/Wells/pages/WellPlanning/utils/calc';

const useCO2EmissionsTargetChart = () => {
  const [{ xLegend }] = useEmissionsTarget();
  const { wellPlanId } = useCurrentWellPlan();
  const { data: baselineCO2Data, isFetching: isFetchingBaselineCO2 } =
    useBaselineCO2Emissions(wellPlanId);
  const { data: targetCO2Data, isFetching: isFetchingTargetCO2 } =
    useTargetCO2Emissions(wellPlanId);
  const { colors } = useTheme();
  const labels: string[] = useMemo(() => {
    const dates = (baselineCO2Data || []).map((data) => data.date);
    if (xLegend === 'days') {
      return dates.map((date, index) => String(index + 1));
    } else if (xLegend === 'dates') {
      return dates.map((date) => format(parseISO(date), DATE_FORMAT_SHORT));
    }
    throw new Error(`Unknown unit type: ${xLegend}`);
  }, [baselineCO2Data, xLegend]);
  const [
    {
      scopes: { scope1, scope2, scope3 },
      scopes,
      lines: { target, baseline },
    },
  ] = useEmissionsTarget();
  const scope1Dataset: ChartDataset<'bar'> | null = useMemo(
    () =>
      scope1
        ? {
            label: 'Scope 1',
            data: (targetCO2Data || []).map(
              (targetCO2) => targetCO2.asset + targetCO2.boilers,
            ),
            backgroundColor: colors.netZeroBlue['3'],
            type: 'bar',
            order: 2,
          }
        : null,
    [colors, scope1, targetCO2Data],
  );
  const scope2Dataset: ChartDataset<'bar'> | null = useMemo(
    () =>
      scope2
        ? {
            label: 'Scope 2',
            data: (targetCO2Data || []).map(
              (targetCO2) => targetCO2.external_energy_supply,
            ),
            backgroundColor: colors.netZeroBlue['6'],
            type: 'bar',
            order: 2,
          }
        : null,
    [colors, scope2, targetCO2Data],
  );
  const scope3Dataset: ChartDataset<'bar'> | null = useMemo(
    () =>
      scope3
        ? {
            label: 'Scope 3',
            data: (targetCO2Data || []).map(
              (targetCO2) =>
                targetCO2.vessels + targetCO2.helicopters + targetCO2.materials,
            ),
            backgroundColor: colors.netZeroBlue['9'],
            type: 'bar',
            order: 2,
          }
        : null,
    [colors, scope3, targetCO2Data],
  );
  const baselineDataset: ChartDataset<'line'> | null = useMemo(
    () =>
      baseline
        ? {
            label: 'Baseline',
            borderColor: colors.blue['7'],
            data: (baselineCO2Data || []).map((baselineCO2) =>
              calculateTotalCO2Emission({ data: baselineCO2, scopes }),
            ),
            type: 'line',
            stack: 'baseline',
            order: 1,
          }
        : null,
    [baseline, baselineCO2Data, colors.blue, scopes],
  );
  const targetDataset: ChartDataset<'line'> | null = useMemo(
    () =>
      target
        ? {
            label: 'Target',
            borderColor: colors.salomn['1'],
            data: (targetCO2Data || []).map((targetCO2) =>
              calculateTotalCO2Emission({ data: targetCO2, scopes }),
            ),
            type: 'line',
            stack: 'target',
            order: 1,
          }
        : null,
    [target, colors.salomn, targetCO2Data, scopes],
  );
  const datasets = useMemo(
    () =>
      ([] as (ChartDataset<'bar'> | ChartDataset<'line'>)[]).concat.apply(
        [],
        [
          scope1Dataset,
          scope2Dataset,
          scope3Dataset,
          targetDataset,
          baselineDataset,
        ].filter(notEmpty),
      ),
    [
      scope1Dataset,
      scope2Dataset,
      scope3Dataset,
      baselineDataset,
      targetDataset,
    ],
  );

  return {
    labels,
    datasets,
    isFetching: isFetchingTargetCO2 || isFetchingBaselineCO2,
  };
};

export default useCO2EmissionsTargetChart;
